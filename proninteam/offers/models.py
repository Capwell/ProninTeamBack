import os

from django.core.mail import EmailMessage
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from offers import AVAILABLE_DATA_TYPES
from offers.api.utils import send_telegram_message

from proninteam.settings import MEDIA_URL

EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_FROM = os.getenv('EMAIL_FROM')


class Offer(models.Model):
    name = models.CharField(
        'Имя',
        validators=[MinLengthValidator(2)],
        max_length=20,
        blank=False,
    )
    communicate = models.CharField(
        'Способ связи',
        validators=[MinLengthValidator(2)],
        max_length=20,
        blank=False,
    )
    message = models.TextField(
        'Сообщение',
        validators=[MinLengthValidator(20)],
        null=False,
        blank=True,
    )
    file = models.FileField(
        'Файл, прикрепленный к заявке',
        validators=[
          FileExtensionValidator(
              allowed_extensions=AVAILABLE_DATA_TYPES
          )
        ],
        upload_to='offers/',
        null=True,
    )
    is_agreed = models.BooleanField(
        'Согласие на обработку персональных данных',
        blank=False,
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

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
