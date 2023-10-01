from orders.models import Order
from robots.models import Robot, ValidRobot
from customers.models import Customer


class OrderService:

    def check_robot_availability(self, model_version_id):
        data = ValidRobot.objects.get(id=model_version_id)
        model = data.model
        version = data.version
        robots = Robot.objects.filter(model=model, version=version, order__isnull=True)
        if not robots.exists():
            return None
        else:
            return robots.first().id

    def create_order(self, robot_id, customer_id):
        customer = Customer.objects.get(id=customer_id)
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
        data = ValidRobot.objects.get(id=model_version_id)
        model = data.model
        version = data.version
        customer = Customer.objects.get(id=customer_id)
        order = Order.objects.create(
            robot_serial=f"{model}-{version}",
            customer=customer,
            status='waiting',
            notified=False
        )
        return order