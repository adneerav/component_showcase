from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, full_name, active=False,
                    staff=False, admin=False, confirmed_email=False):
        if not email:
            raise ValueError("Email required.")
        if not username:
            raise ValueError("Username required.")
        if not password:
            raise ValueError("Password required.")
        if not full_name:
            raise ValueError("Full name required.")
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user_obj.set_password(password)
        user_obj.staff = staff
        user_obj.active = active
        user_obj.admin = admin
        user_obj.full_name = full_name
        user_obj.confirmed_email = confirmed_email
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password, full_name):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            full_name=full_name,
            is_staff=True,
            is_active=True,
            is_confirmed_email=True
        )
        return user

    def create_superuser(self, email, username, password=None, full_name=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            is_staff=True,
            is_admin=True,
            full_name=full_name,
            is_active=True,
            is_confirmed_email=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    confirmed_email = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def get_full_name(self):
        return self.full_name

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
