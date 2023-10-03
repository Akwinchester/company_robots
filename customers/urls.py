from django.urls import path
from customers.views import SignUpView, LoginUser, logout_user

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
