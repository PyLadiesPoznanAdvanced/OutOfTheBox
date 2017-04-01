from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.SearchProfileListView.as_view(), name='list'),
    # url(r'^configure/$', views.configure, name='configure'),
]
