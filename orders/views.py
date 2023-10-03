from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import OrderForm
from .services import OrderService


# def create_order(request):
#     model = 'R2'
#     version = 'D2'
#     customer_id = 1
#
#
#     service = OrderService()
#
#     robot_id = service.check_robot_availability(model, version)
#
#     if robot_id:
#         order = service.create_order(robot_id, customer_id)
#     else:
#         order = service.create_waiting_order(model, version, customer_id)
#
#     return JsonResponse({'status': 'ok'})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            robot_serial_id = form.cleaned_data['robot_serial']

            customer_id = request.user.id

            service = OrderService()

            robot_id = service.check_robot_availability(robot_serial_id)

            if robot_id:
                order = service.create_order(robot_id, customer_id)
            else:
                order = service.create_waiting_order(robot_serial_id, customer_id)

            return render(request, 'home.html', {'form': form})

    else:
        form = OrderForm()

    return render(request, 'home.html', {'form': form})
