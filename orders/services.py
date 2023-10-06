from orders.models import Order
from robots.models import Robot, ValidRobot
from django.contrib.auth.models import User


class OrderService:
    """
    Сервис для работы с заказами
    """

    def check_robot_availability(self, model_version_id):
        """
        Проверяет доступность робота
        """
        data = ValidRobot.objects.get(id=model_version_id)
        model = data.model
        version = data.version
        robots = Robot.objects.filter(
            model=model,
            version=version,
            order__isnull=True
        )
        if not robots.exists():
            return None
        else:
            return robots.first().id

    def create_order(self, robot_id, customer_id):
        """
        Создает заказ со статусом 'available'
        """
        customer = User.objects.get(id=customer_id)
        robot = Robot.objects.get(id=robot_id)
        order = Order.objects.create(
            robot_serial=f"{robot.model}-{robot.version}",
            robot=robot,
            customer=customer,
            status='available',
            notified=True
        )
        return order

    def create_waiting_order(self, model_version_id, customer_id):
        """
        Создает заказ со статусом 'waiting'
        """
        data = ValidRobot.objects.get(id=model_version_id)
        model = data.model
        version = data.version
        customer = User.objects.get(id=customer_id)
        order = Order.objects.create(
            robot_serial=f"{model}-{version}",
            customer=customer,
            status='waiting',
            notified=False
        )
        return order

    def handle_order_creation(self, robot_serial_id, customer_id):
        """
        Обрабатывает создание заказа
        """
        robot_id = self.check_robot_availability(robot_serial_id)

        if robot_id:
            self.create_order(robot_id, customer_id)
            return True
        else:
            self.create_waiting_order(robot_serial_id, customer_id)
            return False