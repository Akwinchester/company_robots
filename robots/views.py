from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Robot

from .services import RobotService


class RobotCreateView(View):

   def post(self, request):
      json_data = request.body

      robot_service = RobotService()
      robot_service.create_from_json(json_data)

      return HttpResponse('Ok')