from django.urls import path , include
from .views import job_detail,job_list

urlpatterns = [
 
    path('', job_list),
    path('<int:id>', job_detail),
]