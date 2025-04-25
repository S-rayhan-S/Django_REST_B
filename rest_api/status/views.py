from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer
from rest_framework import generics

# Create your views here.
class StatusViewer(APIView):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        status=Status.objects.get(pk=id)
        serializer= StatusSerializer(status, many=False)
        return Response(serializer.data)

class StatusListView(generics.ListAPIView):
    # def get(self,request):
    #     all_status=Status.objects.all()
    #     serializer=StatusSerializer(all_status,many=True)
    #     return Response(serializer.data)
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    

class StatusCreateView(generics.CreateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    
class StatusDetailView(generics.RetrieveAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer   
    
class StatusUpdateView(generics.UpdateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer   
    
class StatusDeleteView(generics.DestroyAPIView):  
    queryset=Status.objects.all()
    serializer_class=StatusSerializer   


