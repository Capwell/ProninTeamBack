from django.db import models


class Case(models.Model):
    title = models.CharField(
        'Название',
        max_length=20,
        null=False,
        blank=False
    )
    color = models.CharField(
        'Цвет',
        max_length=7,
        null=False,
        blank=False
    )
    logo = models.ImageField(
        'Лого',
        upload_to='cases/',
        null=False
    )
    is_on_main_page = models.BooleanField(
        'На главной странице?',
        default=False
    )

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
