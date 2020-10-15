from django.urls import path
from .views import cmdvceinvtrlist, cmdvceinvtronerequest, CmDvceInvtrViewset, CmMetalViewset, CmFilterViewset

urlpatterns = [
    path('cm/<int:acct>/', cmdvceinvtrlist, name='cmlist'),
    path('cm/<int:acct>/<int:seq>/', cmdvceinvtronerequest, name='cmone'),
    path('cm/', CmDvceInvtrViewset, name='cmview'),
    path('cm/metal/', CmMetalViewset, name='cmmetal'),
    path('cm/filter/', CmFilterViewset, name='cmfilter')
]