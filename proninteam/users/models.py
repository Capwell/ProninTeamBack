from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.files.base import ContentFile
from django.db import models
from sorl.thumbnail import get_thumbnail


class Role(models.Model):
    title = models.CharField(
        'Название',
        max_length=20
    )

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('У пользователя должен быть указан email')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        'Имя',
        max_length=100,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=100,
    )
    main_role = models.ForeignKey(
        verbose_name='Главная роль',
        to=Role,
        on_delete=models.PROTECT,
        related_name='main_role',
        null=True,
    )
    other_roles = models.ManyToManyField(
        verbose_name='Роли пользователя',
        to=Role,
        related_name='other_roles',
    )
    photo = models.ImageField(
        'Фотография',
        upload_to='users/',
        null=False,
    )
    email = models.EmailField(
        'Email',
        null=False,
        unique=True,
    )
    phone = models.CharField(
        'Номер телефона',
        max_length=15,
        null=False,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        if not self.pk:
            super(User, self).save(*args, **kwargs)
            resized = get_thumbnail(
                self.photo,
                "255x260",
                crop='center',
                quality=51
            )
            with open(f'./media/{resized}', 'rb') as photo:
                self.photo.save(photo.name, ContentFile(resized.read()), True)
        super(User, self).save(*args, **kwargs)
