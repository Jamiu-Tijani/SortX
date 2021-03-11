from django.conf.urls import url 
from . import views 
urlpatterns = [ url(r'^$', views.index),
                   url(r'^action/' ,views.action),
                   url(r'^user_create/', views.user_create),
                   url(r'^index/', views.index2)

                    ]