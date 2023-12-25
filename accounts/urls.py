from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import user_login

urlpatterns = [
    # path('', user_login, name="login"),
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
