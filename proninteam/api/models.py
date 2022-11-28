import os

from django.db import models
from django.core.mail import EmailMessage
from django.core.validators import MinLengthValidator

EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_FROM = os.getenv('EMAIL_FROM')


class Request(models.Model):
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

    def send_request_email(self, file=None):
        mail = EmailMessage(
            subject='Новая Заявка!',
            body=f'{self.name}, {self.communicate}, {self.message}',
            from_email=EMAIL_FROM,
            to=[EMAIL_TO]
        )
        if file:
            mail.attach(file.name, file.file.read(), file.content_type)
        mail.send()
