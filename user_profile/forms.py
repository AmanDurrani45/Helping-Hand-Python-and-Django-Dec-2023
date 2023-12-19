# from django import forms

# from .models import UserProfile

# class ProfileForm(forms.ModelForm):
    # Area = forms.CharField(
        # error_messages={'required': 'Please mention your area!'}
    # )
    # class Meta:
    #     model = Profile 
    #     fields = '__all__'
        # exclude = ("name",)
        # labels = {
        #     "name": "Your name",
        #     "review": 'Your feedback',
        # }

# class CustomerForm(forms.ModelForm):
    # Area = forms.CharField(
        # error_messages={'required': 'Please mention your area!'}
    # )
    # class Meta:
    #     model = Customer 
    #     fields = '__all__'
        # exclude = ("name",)
        # labels = {
        #     "name": "Your name",
        #     "review": 'Your feedback',

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        labels = {
            'user': 'Username', 
            'city': 'City',
            'phone': 'Phone Number',
            'image': 'Profile Picture',
        }
        widgets = {
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        
        }

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']