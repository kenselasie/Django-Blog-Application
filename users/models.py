from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password, **extraarguments):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')

        user = self.model(
            email = self.normalize_email(email),
            # password = password,
            username = username,
            # firstname = firstname,
            # lastname = lastname,
            # phone_num = phone_num,
             **extraarguments
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extraarguments):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            **extraarguments
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
        

class Users(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    firstname = models.CharField(max_length=60, default=None)
    lastname = models.CharField(max_length=60, default=None, null=True)
    othernames = models.CharField(max_length=60, default=None, null=True, blank=True)
    phone_num = models.CharField(max_length=60, unique=True)
    profile = models.CharField(max_length=700, default=None, null=True)
    dependent = models.ForeignKey('self', default=None, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=60, default='Owner')

    username = models.CharField(max_length=60, unique=True) # Required
    is_active = models.BooleanField(default=True) # Required - user can login
    is_staff = models.BooleanField(default=False) # Required
    is_superuser = models.BooleanField(default=False) # Required
    is_admin = models.IntegerField(default=0) # Required
    date_joined = models.DateTimeField(auto_now_add= True) # Required

    objects = MyAccountManager()
    
    USERNAME_FIELD = 'email' # what you want them to login with, and to be represented as
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'phone_num']  # Any extra required field aside email and password 
    EMAIL_FIELD = 'email'   # 

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    class Meta: 
        verbose_name = 'User'