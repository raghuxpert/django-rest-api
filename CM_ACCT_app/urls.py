from django.urls import path
from .views import cmacctlist

urlpatterns = [
    path('cmacct/', cmacctlist, name='cmlist'),
    ]