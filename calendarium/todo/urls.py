from django.urls import path 
from todo import views

urlpatterns = [
    path('', views.index, name='home_todo'),
]

htmxpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
]

urlpatterns += htmxpatterns