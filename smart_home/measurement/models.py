from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    description = models.CharField(max_length=200,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(verbose_name='температура',
                                      max_digits=5,
                                      decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Время фиксации',
                                      auto_now_add=True,)
    sensor_id = models.ForeignKey(Sensor,
                                  on_delete=models.CASCADE,
                                  verbose_name='ID датчика')
    picture = models.ImageField(blank=True, null=True,
                                upload_to='images/')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'{self.temperature} - {self.created_at}'
