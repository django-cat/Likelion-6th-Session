from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('create/', create, name = 'create'),
    path('delete/<int:id>', delete, name = 'delete'),
    path('update/<int:id>', update, name = 'update'),
]

