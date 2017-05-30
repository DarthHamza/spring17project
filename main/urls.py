from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^createCoffee/$', createCoffee, name="createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name="editCoffee"),
]
