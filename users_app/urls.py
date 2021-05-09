from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add-user', views.add_user),
    path('delete/<int:id>', views.delete_user)
]