from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(max_length=10, verbose_name='Температура при измерении')
    date_time = models.DateTimeField(auto_now=True)

# датчик:
#
# название,
# описание (необязательное, например, «спальня» или «корридор на 2 этаже»).

# измерение температуры:
#
# ID датчика,
# температура при измерении,
# дата и время измерения.
