from django.urls import path
from .views import NewUserCreateView, NewSuperUserCreateView


urlpatterns = [
    path('create-user', NewUserCreateView.as_view(), name='create-user'),
    path('create-super-user', NewSuperUserCreateView.as_view(), name='create-super-user'),
]
