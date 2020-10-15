from django.urls import path
from .views import cmacctlist, comment, commentlist, cmacct, cmacctwp

urlpatterns = [
    path('cmacctlist/', cmacctlist, name='cmlist'),
    path('cmacct/<int:pk>/', cmacct, name='cmacct'),
    path('cmacctwp/', cmacctwp, name='cmacct'),
    path('comment/', comment, name='comment'),
    path('commentlist/', commentlist, name='comment'),
    ]