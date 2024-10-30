from django.db import models


# эту таблицу создала сразу верно в django, запросы выполняются
class NewModelDjango(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    dt_birth = models.DateField()
    comment = models.TextField()
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# эту таблицу создала в БД, хотела подключить, не получилось обратиться через shell и admin
class NewTablePostgre(models.Model):
    name = models.CharField(max_length=30)
    discription = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.name

# python manage.py shell
# from homepost.models import *
# NewModelDjango.objects.all()
# a = NewModelDjango.objects.all()
# a.get(id=1)
# a.filter(id=4)
# a[1]
# a.create(name='name_shell', lastname='s', age=18, dt_birth='2006-01-01', comment='k', change_at='2024-10-30')
