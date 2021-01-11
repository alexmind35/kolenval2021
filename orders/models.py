from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    time_order = models.TimeField(auto_now_add=True)
    STATUS_ORDERS = [
        ('1', 'Новый'),
        ('2', 'Отменен'),
        ('3', 'Выполнен')
    ]
    status_order = models.CharField(choices=STATUS_ORDERS, default='1', max_length=1)

    def __str__(self):
        return f'User: {self.user}, {self.get_status_order_display()}'


class Service(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name_service = models.CharField(max_length=255)
    price = models.PositiveIntegerField("Цена")

    def __str__(self):
        return f'Order: {self.order}, {self.name_service}, {self.price}'
