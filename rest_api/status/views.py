from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer
from rest_framework import generics,mixins,parsers
from rest_framework import viewsets
# Create your views here.

class StatusViewSet(viewsets.ModelViewSet):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    parser_classes= [parsers.MultiPartParser, parsers.FormParser ]



##these 2 views(ListCreateAPIView,RetrieveUpdateDestroyAPIView) are use for small tasks & to make coding faster.
# Under the hood they also use mixins. 
# for customized API, views need to be built seperately

# class StatusListCreateApiView(generics.ListCreateAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     parser_classes= [parsers.MultiPartParser, parsers.FormParser ]
    
    
# class StatusDetailDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     parser_classes= [parsers.MultiPartParser, parsers.FormParser ]
    
    


# class StatusListCreateApiView(generics.ListAPIView,mixins.CreateModelMixin):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
    
#     def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
    
# class StatusDetailDeleteUpdateView(generics.RetrieveAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
    
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
#     def update(self,request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# class StatusViewer(APIView):
#     def get(self,request,**kwargs):
#         id=kwargs.get('id')
#         status=Status.objects.get(pk=id)
#         serializer= StatusSerializer(status, many=False)
#         return Response(serializer.data)

# class StatusListView(generics.ListAPIView):
#     # def get(self,request):
#     #     all_status=Status.objects.all()
#     #     serializer=StatusSerializer(all_status,many=True)
#     #     return Response(serializer.data)
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
    

# class StatusCreateView(generics.CreateAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
    
# class StatusDetailView(generics.RetrieveAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer   
    
# class StatusUpdateView(generics.UpdateAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer   
    
# class StatusDeleteView(generics.DestroyAPIView):  
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer   


