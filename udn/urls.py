from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url( r'^advert/$', views.advertise, name='advertise' ),
    url( r'^about_us/$', views.about_us, name='about_us' ),
    url( r'^customer_portal/$', views.customer_portal, name='customer_portal' ),
    url( r'^faqs/$', views.faqs, name='faqs' ),
]
