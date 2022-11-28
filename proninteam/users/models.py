from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class Role(models.Model):
    title = models.CharField('Название', max_length=20)
    is_main = models.BooleanField('Главная ли роль', default=False)


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
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
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100)
    roles = models.ManyToManyField(verbose_name='Роли пользователя', to=Role)
    photo = models.ImageField('Фотография',
                              upload_to='photos/',
                              null=False
                              )
    email = models.EmailField('Email',
                              null=False,
                              unique=True
                              )
    phone = models.CharField('Номер телефона',
                             max_length=15,
                             null=False,
                             unique=True
                             )
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
