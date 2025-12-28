from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..serializers import UserRegisterSerializer
@api_view(['GET','POST'])

def user_views(request):
    if request.method== 'GET':
    
        print("request",request)

        return Response({"message":"Welcome"}, status=status.HTTP_200_OK)

    elif request.method== 'POST':
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors
                        ,status=status.HTTP_400_BAD_REQUEST)