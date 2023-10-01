from django.db import models

from customers.models import Customer

from robots.models import Robot


class Order(models.Model):
    STATUSES = (
        ('available', '1'),
        ('waiting', '0')
    )
    robot_serial = models.CharField(max_length=5,blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='waiting')
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.robot} for {self.customer}"


class ValidRobot:
    pass