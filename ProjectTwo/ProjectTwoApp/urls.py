from django.conf.urls import url
from ProjectTwoApp import views

urlpatterns=[
    url(r'^$',views.users,name='users'),
]
