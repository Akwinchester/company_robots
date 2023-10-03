from django.core.exceptions import ValidationError
from django.db import models

from django.utils.dateparse import parse_datetime



class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.model}-{self.version}"

    def clean_and_validate(self, data):
        if not all(key in data for key in ['model', 'version', 'created', 'serial']):
            raise ValidationError("Invalid data provided")

        created_date = parse_datetime(data['created'])
        if not created_date:
            raise ValidationError("Invalid date format")

        if not ValidRobot.objects.filter(model=self.model, version=self.version).exists():
            raise ValidationError(f'Invalid model {self.model} and version {self.version}')


# def robot_created(sender, instance, created, **kwargs):
#     if created:
#         notification = NotificationService()
#
#         notification.send_notifications(instance)
#
#
# post_save.connect(robot_created, sender=Robot)

class ValidRobot(models.Model):
    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2)

    class Meta:
        unique_together = ('model', 'version')

    def __str__(self):
        return f"{self.model}-{self.version}"