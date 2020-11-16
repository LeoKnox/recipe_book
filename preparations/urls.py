from django.urls import path

from . import views

app_name = 'preparations'
urlpatterns = [
    path('', views.index, name='index'),
]