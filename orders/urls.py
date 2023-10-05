from django.urls import path
from orders.views import OrderView

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create_order'),
]
