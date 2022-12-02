import os

from django.db import models
from django.core.mail import EmailMessage
from django.core.validators import MinLengthValidator

from proninteam.settings import MEDIA_URL

EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_FROM = os.getenv('EMAIL_FROM')


class Offer(models.Model):
    name = models.CharField(
        'Имя',
        validators=[MinLengthValidator(2)],
        max_length=20,
        null=False,
        blank=False
    )
    communicate = models.CharField(
        'Способ связи',
        validators=[MinLengthValidator(2)],
        max_length=20,
        null=False,
        blank=False
    )
    message = models.TextField(
        'Сообщение',
        validators=[MinLengthValidator(20)],
        null=True,
        blank=True
    )
    file = models.FileField(
        'Файл, прикрепленный к заявке',
        upload_to='api/',
        null=True
    )
    is_agreed = models.BooleanField(
        'Согласие на обработку персональных данных',
        null=True
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
            with open(f'{MEDIA_URL}{str(self.file)}', 'rb') as file:
                mail.attach(file.name, file.read())
        mail.send()
