from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from .models import Company

# send  any new User to Default Group
def add_to_default_group(sender,instance,created,**kwards):
   if created:
      group,ok=Group.objects.get_or_create(name='default')
      instance.groups.add(group)
      Company.objects.create(
         user=instance,
      )

post_save.connect(add_to_default_group,sender=User)