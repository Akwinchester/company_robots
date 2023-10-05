import pytest
from unittest.mock import patch
from django.contrib.auth.models import User

from orders.models import Order
from orders.services import OrderService
from robots.models import Robot
from robots.services.notification_service import NotificationService


@pytest.fixture
def order_and_robot():
    # Создание пользователя
    user = User.objects.create_user(
        username='test_user',
        email='test@user.com',
        password='password'
    )

    # Создание робота
    robot_data = {
        "model": "R2",
        "version": "D2",
        "created": "2023-10-10T12:00:00Z"
    }
    robot = Robot.objects.create(model='R2', version='D2', created="2023-10-02 22:59:59")

    # Создание заказа
    order = Order.objects.create(
        customer=user,
        robot=robot
    )
    user.save()
    robot.save()
    order.save()
    service = OrderService()
    order = service.handle_order_creation(
        robot_serial_id,
        user.id)

    return order, robot


@pytest.mark.django_db
class TestNotificationService:

    def test_get_matching_orders(self, order_and_robot):
        order, robot = order_and_robot

        orders = NotificationService().get_matching_orders(robot, Order)

        assert len(orders) == 1
        assert orders[0] == order

    def test_update_order_status(self, order_and_robot):
        order, robot = order_and_robot

        prev_status = order.status

        NotificationService().update_order_status(order, robot)

        order.refresh_from_db()
        assert order.status == 'available'
        assert order.robot == robot
        assert order.notified == True