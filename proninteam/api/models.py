from django.db import models
from django.core.mail import EmailMessage


class Request(models.Model):
    name = models.CharField('Имя',
                            max_length=20,
                            null=False,
                            blank=False
                            )
    communicate = models.CharField('Способ связи',
                                   max_length=20,
                                   null=False,
                                   blank=False
                                   )
    message = models.TextField('Сообщение',
                               null=True,
                               blank=True
                               )
    file = models.FileField('Файл, прикрепленный к заявке',
                            upload_to='files/',
                            null=True
                            )
    is_agreed = models.BooleanField('Согласие на обработку'
                                    ' персональных данных',
                                    null=True)

    def send_request_email(self, file=None):
        mail = EmailMessage(
            subject='Новая Заявка!',
            body=f'{self.name}, {self.communicate}, {self.message}',
            from_email='proninservice@gmail.com',
            to=['proninc@yandex.ru']
        )
        if file:
            mail.attach(file.name, file.file.read(), file.content_type)
        mail.send()
