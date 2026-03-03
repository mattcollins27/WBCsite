from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_prediction, name='submit_prediction'),
    path('submissions/', views.view_submissions, name='view_submissions'),
]