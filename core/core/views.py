from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    client_device_ip = request.META.get('REMOTE_ADDR', None)
    source_code = f'https://github.com/bmyadav91/django-ip-address-lookup'
    context = {
        'client_ip4':client_device_ip,
        'source_code': source_code
    }
    return render(request, 'index.html', context)