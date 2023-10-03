from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Robot

from .services import RobotService


class RobotCreateView(View):

    def post(self, request):
       json_data = request.body
       robot_service = RobotService()
       data = robot_service.create_from_json(json_data)

       robot = Robot(model=data['model'], version=data['version'], created=data['created'], serial=data['serial'])
       robot.clean_and_validate(data)
       robot.save()

       result = HttpResponse('ok')
       return result

    def get(self, request):
       return render(request, 'home.html')