from django import forms

from robots.models import ValidRobot


class OrderForm(forms.Form):
    ROBOT_CHOICES = [(r.id, f"{r.model}-{r.version}") for r in ValidRobot.objects.all()]

    robot_serial = forms.ChoiceField(choices=ROBOT_CHOICES)