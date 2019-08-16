from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'v1/appointments', views.ApiVersionV1_Appointments)
router.register(r'v1/emergency', views.ApiVersionV1_Emergency)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'hello/', views.HelloView.as_view(), name='hello'),
]