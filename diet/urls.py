from django.urls import path
from . import views

app_name = 'diet' 

urlpatterns = [
    path('diet_plan/', views.diet_plan, name='diet_plan'),  # add trailing slash
    path('<int:pk>/', views.diet_detail, name='diet_detail'),
]
