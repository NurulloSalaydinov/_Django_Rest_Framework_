import json
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'data': WomenSerializer(w, many=True).data})
    
    def post(self, request):
        print(request.data)
        # return Response({'status': 200})
        d = request.data
        title = d.get('title')
        content = d.get('content')
        cat_id = d.get('cat_id')
        if title and content and cat_id:
            post_new = Women.objects.create(
                title = title,
                content=content,
                cat_id=cat_id,
            )
            # https://just-watch.club/watch/tt10648342/thor-love-and-thunder-2022/#/flow=w4aDWH+cdn.vddf0.club/s1=mnlove/c_hs=4509073
            return Response({'title': title, 'content': content, 'id': post_new.id})
        else:
            return Response({'error': 'Try Again'})
    def patch(self, request):
        print('Patch: Delete', request.data)

    def put(self, request):
        print('Put: Update', request.data)

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
