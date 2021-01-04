from django.urls import path
from my_app import views


app_name = "my_app"


urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('registeration/', views.registeration, name='registeration'),
]