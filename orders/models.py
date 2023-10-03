from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from robots.models import Robot
from robots.services.notification_service import NotificationService


class Order(models.Model):
    STATUSES = (
        ('available', '1'),
        ('waiting', '0')
    )
    robot_serial = models.CharField(max_length=5,blank=False, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='waiting')
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.robot} for {self.customer}"


def robot_created(sender, instance, created, **kwargs):
    if created:
        notification = NotificationService()

        notification.send_notifications(instance, Order)


post_save.connect(robot_created, sender=Robot)