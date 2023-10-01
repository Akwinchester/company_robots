from django import forms

from robots.models import ValidRobot


class OrderForm(forms.Form):
    ROBOT_CHOICES = [(r.id, f"{r.model}-{r.version}") for r in ValidRobot.objects.all()]

    model_version_id = forms.ChoiceField(choices=ROBOT_CHOICES)