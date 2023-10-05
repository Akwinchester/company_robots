from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import OrderForm
from .services import OrderService
from django.contrib import messages


class OrderView(UserPassesTestMixin, View):

    def get(self, request):
        form = OrderForm()
        return render(request, 'create_order.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)

        if form.is_valid():
            robot_serial_id = form.cleaned_data['robot_serial']
            customer_id = request.user.id

            service = OrderService()
            order = service.handle_order_creation(
                robot_serial_id,
                customer_id
            )

        if order:
            messages.success(self.request, 'Заказ успешно оформлен. Ожидайте получения')
        else:
            messages.success(self.request, f'В данный момент робота нет в наличии. Как только он поступит на склад, мы отправим уведомление на {request.user.email}')
        return redirect('create_order')

    def test_func(self):
        if self.request.user.groups.filter(name='Клиенты').exists():
            return True

        return False
