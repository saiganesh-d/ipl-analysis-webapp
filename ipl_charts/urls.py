from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('extra_runs/', views.extra_runs, name='extra_runs'),
    path('economic_bowler/', views.economic_bowler, name='economic_bowler'),
]
