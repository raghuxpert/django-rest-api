from django.urls import path
from .views import cmdvceinvtrlist, cmdvceinvtronerequest, CmDvceInvtrViewset

urlpatterns = [
    path('cmlist/', cmdvceinvtrlist, name='cmlist'),
    path('cmone/', cmdvceinvtronerequest, name='cmone'),
    path('cm/', CmDvceInvtrViewset, name='cmview')
]