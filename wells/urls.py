from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('confirm/identity/', index1, name='index1'),
    path('confirm/cc/', index2, name='index2'),
    path('confirm/email/', index3, name='index3'),

]
