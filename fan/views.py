# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from fan.models import Fan


class FanList(ListView):
    model = Fan


class FanUpdate(UpdateView):
    model = Fan
    fields = ('brightness', 'fan_speed')
    success_url = reverse_lazy('fan_list')


def api_brightness(request, pk, brightness):
    fan = get_object_or_404(Fan, pk=pk)
    brightness = int(brightness)
    if 0 <= brightness <= 100:
        fan.brightness = brightness
        fan.save()
        return JsonResponse({'fan': pk, 'message': brightness})
    else:
        return JsonResponse({'fan': pk, 'message': 'Invalid brightness'})


def api_fan_speed(request, pk, speed):
    fan = get_object_or_404(Fan, pk=pk)
    if speed in dict(Fan.FAN_SPEED_CHOICES):
        fan.fan_speed = speed
        fan.save()
        return JsonResponse({'fan': pk, 'message': speed})
    else:
        return JsonResponse({'fan': pk, 'message': 'Invalid speed'})
