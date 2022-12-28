from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Case(models.Model):
    """Stores a single case entry."""
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=20,
        blank=False,
    )
    hex_color = models.CharField(
        verbose_name=_('Цвет'),
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
        verbose_name=_('Лого'),
        upload_to='cases/',
        null=False,
    )
    text = models.CharField(
        verbose_name=_('Описание кейса'),
        max_length=100,
    )
    slug = models.CharField(
        verbose_name=_('Ссылка'),
        validators=[
            RegexValidator(
                regex='^[a-z0-9-_]+(?:-[a-z0-9]+)*$',
                message='Строка которую вы ввели не подходит для ссылки!'
            )
        ],
        max_length=20,
    )

    is_on_main_page = models.BooleanField(
        verbose_name=_('Отображать на главной'),
        default=False,
    )
    is_visible = models.BooleanField(
        verbose_name=_('Видимый'),
        default=True,
    )

    def __str__(self) -> str:
        """Return string representation of the object."""
        return f'{self.title}'

    class Meta:
        ordering = ['-id']
        verbose_name = _('Кейс')
        verbose_name_plural = _('Кейсы')
