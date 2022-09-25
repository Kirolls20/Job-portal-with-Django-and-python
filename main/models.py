from django.db import models
from django.contrib.auth.models import User

JOB_TIME=(
   ('Full Time','Full Time'),
   ('Part Time' ,'Part Time'),
   ('Internship','Internship'),
)
SENIORITY_LEVEL=(
   ('Entry Level','Entry Level'),
   ('Junior','Junior'),
   ('Associate','Associate'),
   ('Mid Senior Level','Mid Senior Level'),
   ('Senior','Senior'),
   ('Lead','Lead'),
)

GENDER=(
   ('Male','Male'),
   ('Female','Female'),
   ('Other','Other'),
)


class Company(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   position=models.CharField(max_length=200)
   seniorty_level=models.CharField(choices=SENIORITY_LEVEL,max_length=200)
   job_type=models.CharField(choices=JOB_TIME,max_length=200)
   description=models.TextField()
   Required_experince=models.TextField()
   salary=models.IntegerField(null=True)
   location= models.CharField(max_length=300)
   pub_date=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.position

   class Meta:
      ordering=['-pub_date']



class JobSeeker(models.Model):
   name=models.CharField(max_length=200)
   email=models.EmailField(max_length=200)
   gender=models.CharField(choices=GENDER,max_length=200)
   mobile=models.CharField(max_length=200)
   resume=models.FileField(upload_to ='uploads/',null=True,default=None)
   company=models.ForeignKey(Company,on_delete=models.CASCADE)

   def __str__(self):
      return self.name


class SavedJobs(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   savedjobs= models.ForeignKey(Company,on_delete=models.CASCADE)

   def __str__(self):
      return self.savedjobs.position +" " + self.savedjobs.user.username