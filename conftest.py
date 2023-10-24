import pytest
from orders.models import Order
from django.contrib.auth.models import User
from robots.models import Robot
from django.utils import timezone


# Фикстуры для создания тестовых данных:

@pytest.fixture
def robot():
    # Создаем тестового робота
    return Robot.objects.create(
        serial='R2-D2',
        model='R2',
        version='D2',
        created=timezone.now()
    )


@pytest.fixture
def user():
    # Создаем тестового пользователя
    return User.objects.create(
        username='test_user',
        email='nikolaisinyushkin@gmail.com',
        password='test_password'
    )


@pytest.fixture
def order(robot, user):
    # Создаем тестовый заказ, связанный с роботом и пользователем
    return Order.objects.create(
        robot=robot,
        customer=user
    )

