from django.db import models



from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField, Model, IntegerField, \
    PositiveIntegerField, TextField, OneToOneField, ImageField, CASCADE

from shared.models import CustomUserManager, BaseDateModel


class User(AbstractBaseUser, PermissionsMixin):
    first_name = CharField('first name', max_length=150, blank=True)
    last_name = CharField('last name', max_length=150, blank=True)
    email = EmailField('email address', unique=True)
    balance = PositiveIntegerField('balance', default=0)
    is_staff = BooleanField(
        'staff status',
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = BooleanField(
        'active',
        default=False,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )
    date_joined = DateTimeField('date joined', auto_now_add=True, editable=False)
    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images/", default="default.png")
    bio = models.CharField(max_length=150, blank=True, null=True)
    anonym = models.BooleanField(default=False)

    def __str__(self):
        return str(f"Profile of {str(self.user.first_name)}")
        
# Create your models here.
