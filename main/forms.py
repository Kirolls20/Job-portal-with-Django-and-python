from django import forms 
from django.forms import ModelForm
from .models import *


JOB_TIME=(
   ('Full Time','Full Time'),
   ('Part Time' ,'Part Time'),
   ('Internship','Internship'),
)
class AddJobForm(ModelForm):
   class Meta:
      model=Company
      fields=['position','seniorty_level',
         'job_type','description',
         'Required_experince','salary','location'   
      ]

class ApplyJobForm(ModelForm):
   class Meta:
      model=JobSeeker
      fields=['name','email','gender',
         'mobile',
         'resume' 
      ]
   def __init__(self, *args, **kwargs):
      super(ApplyJobForm, self).__init__(*args, **kwargs)


class ChoicesForm(forms.Form):
   job_times= forms.ChoiceField(choices=JOB_TIME)
   class Meta:

      model= Company
      