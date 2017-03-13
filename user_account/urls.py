from django.conf.urls import url

from . import views

app_name = 'user_account'
urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^login/', views.login_view, "", name='login_view'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^register/', views.register, "", name='register')
]