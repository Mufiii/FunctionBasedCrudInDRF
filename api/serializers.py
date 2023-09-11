from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    print('jh')
    name = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=150)
    print(name,'jhgf')
   
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name' , instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.city = validated_data.get('city' , instance.city)
        instance.save()
        return instance