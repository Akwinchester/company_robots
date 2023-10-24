# from sqlite3 import IntegrityError
#
# import pytest
# from django.core.exceptions import ValidationError
# from django.db import transaction
# from django.utils import timezone
# from .services.robot_service import RobotService
#
# from robots.models import Robot, ValidRobot
#
#
# @pytest.fixture
# def valid_robot(db):
#     """Фикстура для создания ValidRobot"""
#     return ValidRobot.objects.create(model='R2', version='D2')
#
#
# def test_robot_creation(db):
#     """Тестируем создание модели Robot"""
#     robot = Robot.objects.create(
#         serial='R2-D2',
#         model='R2',
#         version='D2',
#         created=timezone.now()
#     )
#
#     assert robot.serial == 'R2-D2'
#     assert robot.model == 'R2'
#     assert robot.version == 'D2'
#     assert isinstance(robot.created, timezone.datetime)
#
# def test_robot_validation(db):
#     """Тестируем валидацию модели Robot"""
#
#     # Проверка формата даты
#     with pytest.raises(ValidationError):
#         Robot.objects.create(
#             serial='R2-D2',
#             model='R2',
#             version='D2',
#             created='01-01-2022'
#         )
#
#     with transaction.atomic():
#         # Проверка существующей модели и версии
#         robot = Robot.objects.create(
#             serial='R2-D2',
#             model='R2',
#             version='D2',
#             created=timezone.now()
#         )
#         assert robot
#
#
#
# def test_robot_str(db):
#     """Тестируем строковое представление модели Robot"""
#     robot = Robot.objects.create(
#         serial='R2-D2',
#         model='R2',
#         version='D2',
#         created=timezone.now()
#     )
#     assert str(robot) == 'R2-D2'
#
#
# def test_valid_robot_creation(db):
#     """Тестируем создание модели ValidRobot"""
#     valid_robot = ValidRobot.objects.create(model='R2', version='D2')
#     assert valid_robot.model == 'R2'
#     assert valid_robot.version == 'D2'