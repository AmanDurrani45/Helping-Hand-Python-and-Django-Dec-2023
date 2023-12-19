from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# from .forms import ProfileForm


# class Profile(models.Model):
#     Name = models.CharField(max_length=191 , default=None)
#     Skill = models.CharField(max_length=191 , default=None)
#     CNIC = models.CharField( max_length=15, default=None, unique=True)
#     Licence = models.CharField( max_length=20, default=None, unique=True)
#     Fee = models.IntegerField(default=None)
#     cell_num =PhoneNumberField(null=False, blank=False, unique=True)
#     experience = models.CharField(max_length=50 , default=None)
#     Area = models.CharField(max_length=50, default=None)
    
#     def __str__(self):
#         return f"{self.Name} ({self.Skill}) ({self.CNIC}) ({self.Licence}) ({self.Fee}) ({self.cell_num}) ({self.experience}) ({self.Area}) "


# class Customer(models.Model):
#     Name = models.CharField(max_length=191 , default=None )
#     cell_num =PhoneNumberField(null=False, blank=False, unique=True)
#     Address =models.CharField(max_length=50 , default=None)

#     def __str__(self):
#         return f"{self.Name} ({self.cell_num}) ({self.Address}) "
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=1000, default="Lahore")  # Capitalize default city name
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = PhoneNumberField(null=False, blank=False, unique=True, validators=[phone_regex])
    image = models.ImageField(default='default.jpg', null=True, upload_to='profile_pics')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} ({self.city}) ({self.phone})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
