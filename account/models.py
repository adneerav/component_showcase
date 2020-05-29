from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from language.models import Language
from technology.models import Technology


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
        if self.is_admin:
            return True
        if self.is_staff:
            if perm == 'account.add_user' or perm == 'account.change_user' or \
                    perm == 'account.delete_user':
                return False
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, help_text="Contributors's first name",
                                 null=False, blank=False)
    nick_name = models.CharField(max_length=50, help_text="Contributors's Nick name",
                                 null=False, blank=False)
    bio = models.TextField(help_text="Contributors bio")
    skype_name = models.CharField(max_length=50, help_text="skype name")
    mobile_number = models.CharField(max_length=15, help_text="Contact(Mobile) number")
    profile_image = models.ImageField(upload_to='uploads/users/profile/', db_column='profile_picture'
                                      , blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name="tech_profiles",
                                          help_text="User may know multiple technology.")
    languages = models.ManyToManyField(Language, related_name="language_profiles",
                                       help_text="User may know multiple language.")
    github_account = models.CharField(max_length=500, help_text="github.com account profile url.")
    stackoverflow_account = models.CharField(max_length=500, help_text="stackoverflow.com account profile url.")
    personal_blog_url = models.CharField(max_length=500, help_text="Personal blog or website url.")
