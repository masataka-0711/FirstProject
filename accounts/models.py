from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    email = models.CharField(max_length=255, unique=True)
    created_at = datetime.timedelta(hours=9)
    created_at = models.DateTimeField(default=timezone.now)
    created_at = datetime.timedelta(hours=9)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
   
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'
        
        
    def get_absolute_url(self):
        return reverse_lazy('accounts:home')