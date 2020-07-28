from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from restApp.models import Test
from rest_framework import viewsets
from restApp.serializers import UserSerializer, GroupSerializer , TestSerializer

# Create your views here.

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

class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Test to be viewed or edited.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer