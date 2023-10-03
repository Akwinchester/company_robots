from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Robot
from datetime import date

from .services.robot_service import RobotService
from .services.report_service import ReportsService


class RobotCreateView(View):

   def post(self, request):
      json_data = request.body

      robot_service = RobotService()
      robot_service.create_from_json(json_data)

      return HttpResponse('Ok')


def download_report(request):
   file = ReportsService().generate_robots_report()
   response = HttpResponse(file, content_type='application/vnd.ms-excel')
   response['Content-Disposition'] = f'attachment; filename=report_{date.today()}.xlsx'
   return response