from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import os

from django.urls import reverse

from fanrf import settings


class Fan(models.Model):
    OFF = 'O'
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'

    FAN_SPEED_CHOICES = (
        (OFF, 'off'),
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    )
    name = models.CharField(max_length=255)
    address = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)])
    smart = models.BooleanField()

    fan_speed = models.CharField(max_length=1, choices=FAN_SPEED_CHOICES, default=OFF)
    brightness = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

    def get_command(self):
        base_command = ' '.join([settings.FANRF,
                                 '--spidev=' + settings.SPIDEV,
                                 '--irq=' + settings.IRQ,
                                 '--shutdown=' + settings.SHUTDOWN,
                                 '--address=' + str(self.address)])
        if self.smart:
            return ' '.join([base_command, 'smart', self.get_fan_speed_display(), str(self.brightness)])
        else:
            return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        cmd = self.get_command()
        if settings.DEBUG:
            print(cmd)
        else:
            os.system(cmd)
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('fan_update', kwargs={'pk': self.pk})
