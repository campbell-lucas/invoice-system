from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models


class CustomAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must provide a valid email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        if not user.is_collector:
            sales_manager_group = Group.objects.get(name='sales_managers')
            user.groups.add(sales_manager_group)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        user.is_active = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_collector = models.BooleanField(default=False)
    is_sales_manager = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    objects = CustomAccountManager()
