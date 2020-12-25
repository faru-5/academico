from django.urls import path
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout_prompt/', logout_prompt, name='logout_prompt'),
    path('register/', register, name='register'),

    #profile
    path('', profile, name='user_profile'),
    # password changing url
    path('password/change/', UserPasswordChange.as_view(), name='password_change'),
    path('password/change/done/', UserPasswordChangeDone.as_view(), name='password_change_done'),
]