from django.urls import path
from adoteme.views.views_homepage import index
from adoteme.views.views_auth import register_user, user_registration_done


urlpatterns = [
    path('', index, name='home'),
    path('registration/register_user', register_user, name='register_user'),
    path('registration/registration_done', user_registration_done, name='registration_done'),
]