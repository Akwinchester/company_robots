from django import forms

from robots.models import ValidRobot


class RobotForm(forms.Form):
    ROBOT_CHOICES = [(f"{r.model}-{r.version}", f"{r.model}-{r.version}") for r in ValidRobot.objects.all()]

    serial = forms.ChoiceField(choices=ROBOT_CHOICES)
    created = forms.DateTimeField()
