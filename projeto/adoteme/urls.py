from django.urls import path
from adoteme.views.views_homepage import index


urlpatterns = [
    path('', index, name='index')
]