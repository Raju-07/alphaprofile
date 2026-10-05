from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
import uuid


# Base User manager
class CustomerUserManager(BaseUserManager):
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email must be provided.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    
    def create_superuser(self,email,password=None, ** extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_admin',False)

        
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile-pictures/",blank=True,null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email
    


