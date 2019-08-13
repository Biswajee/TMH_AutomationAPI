from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^image_list/', views.gallery_display, name = 'image_list'),
    url(r'^hello/', views.HelloView.as_view(), name='hello'),
]
