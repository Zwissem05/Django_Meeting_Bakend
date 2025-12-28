from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Meeting

class MeetinSerialzer(serializers.ModelSerializer):
     user = serializers.PrimaryKeyRelatedField(read_only=True)  # rend user non obligatoire

     class Meta:
          model=Meeting
          fields= '__all__'
     def create(self,validated_data):
            meeting=Meeting.objects.create(
            title=validated_data['title'],
            user=self.context['request'].user,

            )
            return meeting
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email','password']
     
    password = serializers.CharField(write_only = True)

    def create(self,validated_data):
            user=User.objects.create_user(
                username=validated_data['username'],
                email= validated_data['emaile'],
                password=validated_data['password']
            )
            return user


