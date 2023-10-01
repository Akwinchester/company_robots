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
        if not all(key in data for key in ['model', 'version', 'created']):
            raise ValidationError("Invalid data provided")

        created_date = parse_datetime(data['created'])
        if not created_date:
            raise ValidationError("Invalid date format")