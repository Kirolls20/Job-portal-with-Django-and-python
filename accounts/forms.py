from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER=(
   ('Male','Male'),
   ('Female','Female'),
   ('Other','Other'),
)

class CreateUserForm(UserCreationForm):
   first_name=forms.CharField(max_length=120)
   last_name=forms.CharField(max_length=120)
   phone_number=forms.CharField(max_length=15)
   gender=forms.ChoiceField(choices=GENDER)

   class Meta:
      model=User
      fields=['first_name','last_name','username','gender','phone_number','email']

