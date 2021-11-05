from django.shortcuts import render, redirect
from .models import Users, Project, Portfolio
from django.http import JsonResponse
from rest_framework import generics
from .serializers import UserSerializer, ProjectSerializer, PortfolioSerializer
# Create your views here.

# Create
class UserShow(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class PortfolioShow(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ProjectShow(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Retrive Update Destroy

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class PortfolioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

