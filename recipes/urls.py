from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<recipe_id>/', views.edit, name='edit'),
    path('detail/<recipe_id>/', views.detail, name='detail'),
    path('delete/<recipe_id>', views.delete, name='delete'),
]