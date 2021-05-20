from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Lot
from .serializers import UserSerializer, LotSerializer
# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
