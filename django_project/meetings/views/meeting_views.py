from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..serializers import MeetinSerialzer
@api_view(['GET','POST'])

def meeting_views(request):
    if request.method== 'GET':
    
        print("request",request)

        return Response({"message":"Welcome dans creating meetings"}, status=status.HTTP_200_OK)

    elif request.method== 'POST':
        serializer=MeetinSerialzer(
            data=request.data,
            context={'request': request} 
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors
                        ,status=status.HTTP_400_BAD_REQUEST)