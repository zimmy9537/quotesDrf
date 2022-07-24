from email.quoprimime import quote
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import Quotelist
from .serializers import QuoteSerializer

# Create your views here.


class QuoteList(generics.ListAPIView):
    serializer_class=QuoteSerializer
    
    def get_queryset(self):
        return Quotelist.objects.all()

class QuoteCreate(APIView):
    def post(self,request):
        serializer=QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={}
            data['response']='quote posted successfully'
            return Response(data)
        else :
            data={}
            data['response']='error while posting'
            return Response(data)

class QuoteDetails(APIView):
    def get(self,request,pk):
        try:
            quote=Quotelist.objects.get(pk=pk)
            serializer=QuoteSerializer(quote)
            return Response(serializer.data)
        except Quotelist.DoesNotExist:
            data={}
            data['response']='no such id exists'
            return Response(data)
        
    def put(self,request,pk):
        quote=Quotelist.objects.get(pk=pk)
        serializer=QuoteSerializer(quote,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response':'updated successfully'})
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            if request.method=='DELETE':
                movie=Quotelist.objects.get(pk=pk)
                movie.delete()
                return Response({'response':'deletion successfull'})
            return Response({'response':'deletion not allowed'})
        except Quotelist.DoesNotExist:
            return Response({'response':'quote does not exist'})