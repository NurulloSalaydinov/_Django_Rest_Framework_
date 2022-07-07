from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer
# from django.shortcuts import render


class WomenAPIView(APIView):
    def get(self, request):
        ls = Women.objects.all().values()
        return Response({'objects': ls})
        # pass
    # pass

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
