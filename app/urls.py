from django.urls import path, include
from .views import dashboard,signup,profile,join_hood,leave_hood

urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('profile/<username>/', profile, name='profile'),
    path('join_hood/<id>', join_hood, name='join-hood'),
    path('leave_hood/<id>', leave_hood, name='leave-hood'),
]