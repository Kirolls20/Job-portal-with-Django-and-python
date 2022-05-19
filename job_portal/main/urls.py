from django.urls import path
from . import  views

urlpatterns=[
    path('',views.AllJobsView.as_view(),name='home'),
    path('hr/home/',views.HrHomeView.as_view(),name='hr-home'),
    path('create/job/hr/',views.AddJobView.as_view(),name='add-new-job'),
    path('job/<int:pk>/',views.JobDetailView.as_view(),name='job_details'),
    path('job/apply<int:pk>/',views.JobApplyView.as_view(),name='job_apply'),
    path('delete/candidate/<int:pk>/',views.DeleteCandidatesView.as_view(),name='delete_candidate'),
    path('delete/job/<int:pk>/',views.DeleteJobView.as_view(),name='delete_job'),
    path('update/job/<int:pk>',views.UpdateJobView.as_view(),name='update_job'),
    path('saved-list/',views.SavedListView.as_view(),name='saved_list'),
    path('save-job/<int:pk>/',views.SaveJobView.as_view(),name='save_job'),
]