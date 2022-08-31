from django.urls import path
from . import views


app_name = 'simple_view'
urlpatterns = [
    path('', views.index),
    path('<int:pk>/name/', views.NameView.as_view()),
    path('<int:q_id>/age/', views.age),
    path('likes/name', views.NameView.as_view(), kwargs={'pk': 2}, name='crush')
]