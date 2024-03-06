from django.urls import path,include
from .import views

urlpatterns = [
    path('register/', views.UserSignupView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]

