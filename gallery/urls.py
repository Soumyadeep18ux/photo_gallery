from django.urls import path
from . import views

urlpatterns = [
    
    path('upload/', views.upload_photo, name='upload_photo'),
    path('user-photos/', views.user_photos, name='user_photos'),
    path('Login/',views.Login, name='Login'),
    path('Signup/',views.Signup, name='Signup'),
    path('Logout/',views.LogoutPage, name='Logout'),
]
