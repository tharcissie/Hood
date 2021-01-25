from django.urls import path, include
from .views import dashboard,signup,profile

urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('profile/<username>/', profile, name='profile'),
]