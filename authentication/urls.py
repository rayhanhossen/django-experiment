from django.urls import path

from authentication.views import UserLoginView

urlpatterns = [
    path('user/login', UserLoginView.as_view(), name='user-login')
]
