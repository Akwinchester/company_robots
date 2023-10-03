from django.urls import path
from robots.views import RobotCreateView, download_report

urlpatterns = [
    path('create_robot/', RobotCreateView.as_view(), name='create_robot'),
    path('download_report/', download_report, name='download_report')
]
