from django.urls import path
from . import views

urlpatterns = [ path("", views.home, name="home"),
    path('history/', views.history, name='history'),
    path('pastprojects/', views.pprojects, name='pprojects'),
    path('futureprojects/', views.fprojects, name='fprojects'),
    path('reachus/', views.reachus, name='reachus'),
 ]

