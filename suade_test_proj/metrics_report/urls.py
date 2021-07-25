from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Suade-test-home'), 
    path('report/', views.report, name='Suade-test-report'), 
    path('result/<date>', views.result, name='Suade-test-report'), 
]
