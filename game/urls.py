from django.urls import path

from . import views


app_name = 'game'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('gaming/', views.GamingView.as_view(), name="gaming"),
    path('results/', views.ResultsView.as_view(), name="results"),
]
