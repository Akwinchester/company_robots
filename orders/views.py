from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import OrderForm
from .services import OrderService
from django.contrib import messages


class OrderView(UserPassesTestMixin, View):
    """
    Представление для создания заказа
    """

    def get(self, request):
        """Отображает форму создания заказа"""
        form = OrderForm()
        return render(request, 'create_order.html', {'form': form})

    def post(self, request):
        """Обрабатывает отправку формы и создание заказа"""
        form = OrderForm(request.POST)

        if form.is_valid():
            robot_serial_id = form.cleaned_data['robot_serial']
            customer_id = request.user.id

            service = OrderService()
            order_message = service.handle_order_creation(robot_serial_id, customer_id)

            messages.success(self.request, order_message)

        return redirect('create_order')

    def test_func(self):
        """Проверяет, что пользователь в группе Клиенты"""
        return self.request.user.groups.filter(name='Клиенты').exists()