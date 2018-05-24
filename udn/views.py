from django.shortcuts import render

from api.models import *


def home(request):

    return render(request, 'udn/home.html', {})

def advertise(request):
    return render(request, 'udn/advertise.html', {})

def about_us(request):
    return render(request, 'udn/about_us.html', {})

def customer_portal(request):
    username = None
    if request.user.is_authenticated():
        username =request.user.username
        informations=Information.objects.filter(advertiser_name=username).order_by('android_id', '-time')
        a=0
        v=0
        for i in informations:
           if a!= int(i.android_id):
             a= int(i.android_id)
             v=v+int(i.video_count)
    return render(request, 'udn/customer_portal.html',{'v': v})
def faqs(request):
    return render(request, 'udn/faqs.html', {})