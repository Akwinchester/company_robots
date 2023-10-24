# from django.core.exceptions import ValidationError
#
# import pytest
# from .models import Order
#
#
# # Простой тест заказа
# @pytest.mark.django_db
# def test_order(order):
#     # Проверяем поля заказа
#     assert order.robot.serial == 'R2-D2'
#     assert order.customer.username == 'test_user'
#
#
# # Класс с юнит-тестами для модели Order
# @pytest.mark.django_db
# class TestOrder:
#
#     # Тест получения объекта по id
#     def test_get_order_by_id(self, order):
#         received_order = Order.objects.get(id=order.id)
#         assert received_order == order
#
#     # Тест __str__
#     def test_order_string_representation(self, order):
#         assert str(order) == f'Заказ {order.id} - {order.robot} для {order.customer}'
#
#     # Тест валидации полей
#     def test_field_validation(self):
#         with pytest.raises(ValidationError):
#             order = Order(robot_serial='')
#             order.full_clean()
#
#     # Тест значений по умолчанию
#     def test_default_values(self, order):
#         assert order.status == 'waiting'
#         assert order.notified == False
#
#     # Тест связей с другими моделями
#     def test_relationships(self, order, robot, user):
#         assert order.robot == robot
#         assert order.customer == user