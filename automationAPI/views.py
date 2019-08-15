from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ApiVersionV1_Appointments, ApiVersionV1_Emergency
from .models import appointments


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# sample model...
class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ApiVersion_v1(viewsets.ModelViewSet):

    queryset = appointments.objects.all()
    serializer_class = ApiVersionV1_Appointments

    def get_appointments(self, request):
        queryset = self.queryset.filter()
        return queryset

    def emergency_bookings(self, request):
        queryset = emergency.objects.all()
        serializer_class = ApiVersionV1_Emergency
        queryset = self.queryset.filter()
        return queryset
