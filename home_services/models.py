from django.db import models

# from geoposition.fields import GeopositionField

from phonenumber_field.modelfields import PhoneNumberField



class Service(models.Model):
    ServiceName = models.CharField(max_length=191 , default=None)
    Title = models.CharField(max_length=191 , default=None)
    # Discription = models.CharField(max_length=191)
    Price = models.IntegerField(default=None)
    # cell_num =PhoneNumberField(null=False, blank=False, unique=True)
    # experience = models.CharField(max_length=50 , default=None)
    
    def __str__(self):
        return f"{self.ServiceName} ({self.Title}) <{self.Price}>"
    
class Profile(models.Model):
    Name = models.CharField(max_length=191 , default=None)
    Skill = models.CharField(max_length=191 , default=None)
    CNIC = models.CharField( max_length=15, default=None, unique=True)
    Licence = models.CharField( max_length=20, default=None, unique=True)
    Fee = models.IntegerField(default=None)
    cell_num =PhoneNumberField(null=False, blank=False, unique=True)
    experience = models.CharField(max_length=50 , default=None)
    Area = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return f"{self.Name} ({self.Skill}) ({self.CNIC}) ({self.Licence}) ({self.Fee}) ({self.cell_num}) ({self.experience}) ({self.Area}) "


class Customer(models.Model):
    Name = models.CharField(max_length=191 , default=None )
    cell_num =PhoneNumberField(null=False, blank=False, unique=True)
    Address = models.CharField(max_length=50)
    ServiceTitle = models.CharField(max_length=50)
    TimeAndDate = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.Name} ({self.cell_num}) ({self.Address}) ({self.ServiceTitle}) ({self.TimeAndDate}) "
    
# class User_profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     # bio = models.CharField(max_length=1000)
#     city = models.CharField(max_length=1000, default="lahore")
#     phone = models.IntegerField(null=True, blank=True)
#     image = models.ImageField( default='default.jpg',null= True, upload_to='profile_pic' )
#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f'{self.user.username}'
    
# class Location(models.Model):
#     name = models.CharField(max_length=255)
#     coordinates = GeopositionField()

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
