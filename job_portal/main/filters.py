import django_filters
from .models import *

class JobFilters(django_filters.FilterSet):
   class Meta:
      model = Company
      fields= ['seniorty_level','job_type','position']
