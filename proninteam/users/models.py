from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import get_thumbnail


class Role(models.Model):
    """Stores a single user role entry."""
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=20
    )

    def __str__(self):
        """Return string representation of the object."""
        return f'{self.title}'

    class Meta:
        ordering = ['-id']
        verbose_name = _('Роль')
        verbose_name_plural = _('Роли')


class UserManager(BaseUserManager):
    """
    Custom user manager.
    Validate data and create new user entry.
    """
    def _create_user(self, email, password, **kwargs):
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        """Creating a user."""
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """Creating a superuser."""
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs
        )


class User(AbstractBaseUser, PermissionsMixin):
    """
    Stores a single custom user entry,
    related to :model:`users.Role`

    Required fields:
    - email, phone,
      first_name, middle_name, last_name,
      main_role, other_roles, photo.
    """
    email = models.EmailField(
        verbose_name=_('Email'),
        null=False,
        unique=True,
    )
    phone = models.CharField(
        verbose_name=_('Номер телефона'),
        max_length=15,
        null=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('Имя'),
        max_length=100,
    )
    middle_name = models.CharField(
        verbose_name=_('Отчество'),
        max_length=100,
    )
    last_name = models.CharField(
        verbose_name=_('Фамилия'),
        max_length=100,
    )
    main_role = models.ForeignKey(
        verbose_name=_('Главная роль'),
        to=Role,
        on_delete=models.PROTECT,
        related_name='main_role',
        null=True,
    )
    other_roles = models.ManyToManyField(
        verbose_name=_('Роли пользователя'),
        to=Role,
        related_name='other_roles',
    )
    photo = models.ImageField(
        verbose_name=_('Фотография'),
        upload_to='users/',
        null=False,
    )
    is_staff = models.BooleanField(
        verbose_name=_('Cтатус сотрудника'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Статус активного аккаунта'),
        default=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone',
        'first_name',
        'middle_name',
        'last_name',
    ]

    objects = UserManager()

    @property
    def is_admin(self) -> bool:
        """Declare that it can be accessed like it's a regular property."""
        return bool(self.is_superuser)

    def __str__(self) -> str:
        """Return string representation of the object."""
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs) -> None:
        """Validate and save photo to field."""
        if not self.pk:
            super(User, self).save(*args, **kwargs)
            resized = get_thumbnail(
                self.photo,
                "255x260",
                crop='center',
                quality=51,
            )
            with open(f'./media/{resized}', 'rb') as photo:
                self.photo.save(
                    photo.name,
                    ContentFile(resized.read()),
                    True
                )
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
