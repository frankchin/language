from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^about/', views.about, name='about'),           
    url(r'^', views.main, name='main'),
]
