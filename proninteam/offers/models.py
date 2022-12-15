import os

from django.core.mail import EmailMessage
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from offers import AVAILABLE_DATA_TYPES
from offers.api.utils import send_telegram_message
from proninteam.settings import MEDIA_URL

EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_FROM = os.getenv('EMAIL_FROM')


class Offer(models.Model):
    """Stores a single offer entry."""
    name = models.CharField(
        verbose_name=_('Имя'),
        validators=[MinLengthValidator(2)],
        max_length=20,
        blank=False,
    )
    communicate = models.CharField(
        verbose_name=_('Способ связи'),
        validators=[MinLengthValidator(2)],
        max_length=20,
        blank=False,
    )
    message = models.TextField(
        verbose_name=_('Сообщение'),
        validators=[MinLengthValidator(20)],
        null=False,
        blank=True,
    )
    file = models.FileField(
        verbose_name=_('Файл, прикрепленный к заявке'),
        validators=[
          FileExtensionValidator(
              allowed_extensions=AVAILABLE_DATA_TYPES
          )
        ],
        upload_to='offers/',
        null=True,
    )
    is_agreed = models.BooleanField(
        verbose_name=_('Согласие на обработку персональных данных'),
        blank=False,
        null=False,
        default=False,
    )

    def send_offer_email(self):
        mail = EmailMessage(
            subject='Новое Предложение!',
            body=f'{self.name}, {self.communicate}, {self.message}',
            from_email=EMAIL_FROM,
            to=[EMAIL_TO]
        )
        if self.file:
            with open(f'.{MEDIA_URL}{str(self.file)}', 'rb') as file:
                mail.attach(file.name, file.read())
        mail.send()
        
    def send_offer_telegram(self):
        message = (
            f'Представьтесь: {self.name}\n'
            f'Способ связи: {self.communicate}\n'
            )
        if self.message:
            message += f'Сообщение: {self.message}\n'
        if self.file:
            message += 'Файл отправлен на почту!'
        send_telegram_message(message)   

    def __str__(self) -> str:
        """Return string representation of the object."""
        return f'{self.name}'

    class Meta:
        ordering = ['-id']
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')
