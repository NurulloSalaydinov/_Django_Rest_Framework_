from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
# from django.shortcuts import render

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
