from django.urls import path

from .views import NewUserCreateView, NewSuperUserCreateView

urlpatterns = [
    path('create', NewUserCreateView.as_view(), name='create-user'),
    path('create/superuser', NewSuperUserCreateView.as_view(), name='create-super-user'),
]
