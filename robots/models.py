from django.core.exceptions import ValidationError
from django.db import models
from django.utils.dateparse import parse_datetime


class Robot(models.Model):
    """Модель Robot - робот"""

    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.model}-{self.version}"

    def clean_and_validate(self, data):
        """Валидирует данные при создании Robot"""
        if not all(key in data for key in ['model', 'version', 'created', 'serial']):
            raise ValidationError("Некорректные данные")

        created_date = parse_datetime(data['created'])
        if not created_date:
            raise ValidationError("Неверный формат даты")

        if not ValidRobot.objects.filter(model=self.model,
                                         version=self.version).exists():
            raise ValidationError(f"Недопустимая модель {self.model} и версия {self.version}")

    def clean(self):
        if not self.serial:
            raise ValidationError('Serial is required')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class ValidRobot(models.Model):
    """Модель допустимых моделей и версий роботов"""

    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2)

    class Meta:
        unique_together = ('model', 'version')

    def __str__(self):
        return f"{self.model}-{self.version}"