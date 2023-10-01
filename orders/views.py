from django.http import JsonResponse
from django.shortcuts import render
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
            print(form.cleaned_data)
            model_version_id = form.cleaned_data['model_version_id']

            customer_id = 1

            service = OrderService()

            robot_id = service.check_robot_availability(model_version_id)

            if robot_id:
                order = service.create_order(robot_id, customer_id)
            else:
                order = service.create_waiting_order(model_version_id, customer_id)

            return render(request, 'home.html', {'form': form})

    else:
        form = OrderForm()

    return render(request, 'home.html', {'form': form})