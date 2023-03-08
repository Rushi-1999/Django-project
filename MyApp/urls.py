from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.index, name= "Home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    # path('upload', views.Uploadcsv, name="upload"),
    # path('Verify',views.Verify_Data), 
    
    ]


