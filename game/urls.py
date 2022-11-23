from django.urls import path

from . import views


app_name = 'game'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('title/', views.TitleView.as_view(), name="title"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('gaming/', views.GamingView.as_view(), name="gaming"),
    path('results/', views.ResultsView.as_view(), name="results"),
]
