from django.core.validators import RegexValidator
from django.db import models


class Case(models.Model):
    title = models.CharField(
        'Название',
        max_length=20,
        blank=False,
    )
    hex_color = models.CharField(
        'Цвет',
        validators=[
            RegexValidator(
                regex='^#(?:[0-9a-fA-F]{3}){1,2}$',
                message='Цвет должен быть в формате HEX',
            ),
        ],
        max_length=7,
        blank=False,
    )
    logo = models.ImageField(
        'Лого',
        upload_to='cases/',
        null=False,
    )
    text = models.CharField(
        'Описание кейса',
        max_length=100,
    )
    slug = models.CharField(
        'Ссылка',
        validators=[
            RegexValidator(
                regex='^[a-z0-9-_]+(?:-[a-z0-9]+)*$',
                message='Строка которую вы ввели не подходит для ссылки!'
            )
        ],
        max_length=20,
    )
    is_on_main_page = models.BooleanField(
        'На главной странице?',
        default=False,
    )
    is_visible = models.BooleanField(
        'Видимый ли?',
        default=True,
    )

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
