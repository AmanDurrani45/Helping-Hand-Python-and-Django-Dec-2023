from django import forms

from .models import *

class ProfileForm(forms.ModelForm):
    # Area = forms.CharField(
        # error_messages={'required': 'Please mention your area!'}
    # )
    class Meta:
        model = Profile 
        fields = '__all__'
        # exclude = ("name",)
        # labels = {
        #     "Name": "Your Name",
        #     "Skill": 'Your Skill',
        # }

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer 
        fields = '__all__'
        widgets = {
            'TimeAndDate': forms.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'Select Date and Time'}),
            'Name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'cell_num': forms.TextInput(attrs={'placeholder': 'Enter Cell Number'}),
            'Address': forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'ServiceTitle': forms.TextInput(attrs={'placeholder': 'Enter Service Title'}),
        }


# class UserProfile(forms.ModelForm):
#     # Area = forms.CharField(
#         # error_messages={'required': 'Please mention your area!'}
#     # )
#     class Meta:
#         model = User_profile
#         fields = '__all__'
#         # exclude = ("name",)
#         # labels = {
#         #     "Name": "Your Name",
#         #     "Skill": 'Your Skill',
#         # }


# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['name', 'coordinates']




class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactSubmissionForm, self).__init__(*args, **kwargs)
        # Add any additional customization for your form fields here, if needed
        # For example, you can set placeholders or additional attributes
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your Message', 'rows': 4})