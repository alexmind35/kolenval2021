from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    name_service = models.CharField(max_length=255)
    price = models.PositiveIntegerField("Цена")

    def __str__(self):
        return f'Service: {self.name_service}, {self.price}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    time_order = models.TimeField(auto_now_add=True)
    STATUS_ORDERS = [
        ('1', 'Новый'),
        ('2', 'Отменен'),
        ('3', 'Выполнен')
    ]
    status_order = models.CharField(choices=STATUS_ORDERS, default='1', max_length=1)

    def __str__(self):
        return "User: {}, Service: {}, status_order: {}".format(self.user, self.service, self.get_status_order_display())
