from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views import View
from .models import *
from .filters import JobFilters
from .forms import AddJobForm,ApplyJobForm,ChoicesForm
from django.contrib import messages 

class HrHomeView(LoginRequiredMixin,TemplateView):
   template_name='hr_home.html'

   def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      context['seekers'] = JobSeeker.objects.all()
   
      return context

class AddJobView(LoginRequiredMixin,CreateView):
   template_name = 'add-job.html'
   form_class = AddJobForm

   def form_valid(self,form):
      obj=form.save(commit=False)
      obj.user=self.request.user
      obj.save()
      return super(AddJobView,self).form_valid(form)
   
   def get_success_url(self):
      return reverse_lazy('home')



class AllJobsView(TemplateView):
   template_name='home.html'
   def  get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Render All Existed Jobs 
      context["alljobs"] = Company.objects.all()
      # Render The FIlter Form
      context['myfilter'] = JobFilters(self.request.GET,queryset= context["alljobs"])
      # render the filter Results
      context["alljobs"] = context['myfilter'].qs
      return context

class JobDetailView(DetailView):
   template_name='job-details.html'
   model=Company
   context_object_name='job'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['count'] = JobSeeker.objects.filter(company=self.kwargs['pk']).count()
      return context


class JobApplyView(CreateView):
   template_name='job-apply.html'
   model = JobSeeker
   form_class=ApplyJobForm
   
   def post(self,request,pk):
      # job_id= Company.objects.get(id=pk)
      job_id=get_object_or_404(Company,id=pk)
      #Note  MUST Store the form in new varible 
      form= ApplyJobForm(request.POST,request.FILES)
      if form.is_valid():
         job_form = form.save(commit=False)
         job_form.company = job_id
         job_form.save()
         return redirect(reverse_lazy('home'))
      return render(request,self.template_name,{'form':form})


# Delete Not Qulified Canditates (Only Recruiter)
class DeleteCandidatesView(LoginRequiredMixin,DeleteView):
   template_name= 'delete_candidate.html'
   model= JobSeeker

   def get_success_url(self):
      return reverse_lazy('hr-home')

# Delete Existed Job (Only Recruiter)
class DeleteJobView(LoginRequiredMixin,DeleteView):
   template_name='delete_job.html'
   model=Company 

   def get_success_url(self):
      return reverse_lazy('home')

# Update The Job Details 
class UpdateJobView(LoginRequiredMixin,UpdateView):
   template_name='update_job.html'
   queryset=Company.objects.all()
   form_class = AddJobForm
   def get_success_url(self):
      return reverse('job_details',kwargs={'pk' : self.object.pk})

class SaveJobView(LoginRequiredMixin,TemplateView):
   template_name='home.html'
   def post(self,request,pk):
      job_id=get_object_or_404(Company,id=pk)
      if request.method == 'POST':
         save_job= SavedJobs(user=self.request.user,savedjobs=job_id)
         if SavedJobs.objects.filter(user=self.request.user,savedjobs=job_id).exists() :
            messages.error(self.request, "This job already exists On Your List!")
            return redirect(reverse_lazy('home'))
         else:
            saved_job=save_job.save()
            messages.success(self.request, "The Job added To your saved Jobs List !")
            return redirect(reverse_lazy('home')) 
      return render(request,self.template_name)


class SavedListView(LoginRequiredMixin,TemplateView):
   template_name='saved_jobs.html'
   
   def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      context['saved_jobs'] = SavedJobs.objects.filter(user=self.request.user)
      return context