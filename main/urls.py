from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^createCoffee/$', createCoffee, name="createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name="editCoffee"),
    url(r'^createBean/$', createBean, name="createBean"),
    url(r'^editBean/(?P<bean_id>[0-9]+)/$', editBean, name="editBean"),
    url(r'^deleteBean/(?P<bean_id>[0-9]+)/$', deleteBean, name="deleteBean"),
]
