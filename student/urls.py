from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('Create/', views.Create, name='Create'),
    path('add_students/',views.add_studnet, name='add_students'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
]