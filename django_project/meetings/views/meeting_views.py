from django.shortcuts import render
from django.utils.timezone import now 
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers import MeetinSerialzer
from ..models import Meeting

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def meeting_views(request):
    if request.method== 'GET':
    
        print("request",request)

        return Response({"message":"Welcome dans creating meetings"}, status=status.HTTP_200_OK)

    elif request.method== 'POST':
        serializer=MeetinSerialzer(data=request.data) 
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors
                        ,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updatemeeting(request):
    date=now().date()
    print(request.data.get('title'))
    print(request.user)

    obj=Meeting.objects.filter(user=request.user,title=request.data.get('title')).first()
    if not obj:
        return Response({"detail":"no meeting with that name was found"},status=status.HTTP_404_NOT_FOUND)
    if obj.date != date:
        return Response({"detail":"you can update just the meetings of today"},status=status.HTTP_400_BAD_REQUEST)

    serializer=MeetinSerialzer(obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


