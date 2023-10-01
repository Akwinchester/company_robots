from django.urls import path
from robots.views import RobotCreateView

urlpatterns = [
    path('create_robot/', RobotCreateView.as_view(), name='create_robot'),
]
