from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import *

class CreateUserView(CreateView):
   template_name ='registration/sign-up.html'
   model=User
   form_class = CreateUserForm

   def get_success_url(self):
      return reverse_lazy('login')