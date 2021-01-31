from django.urls import path, include
from .views import dashboard,signup,profile,join_hood,leave_hood,hood,post,business,search_hood

urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('profile/<username>/', profile, name='profile'),
    path('join_hood/<id>', join_hood, name='join-hood'),
    path('leave_hood/<id>', leave_hood, name='leave-hood'),
    path('hood/<id>', hood, name='hood'),
    path('<id>/create_post', post, name='post'),
    path('<id>/create_business', business, name='business'),
    path('search/', search_hood, name='search'),
]