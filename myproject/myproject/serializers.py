from rest_framework import serializers 
from .models import Array,ArrayToReturn
 
 
class ArraySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Array
        fields = ('input',)

class ArrayToReturnSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ArrayToReturn
        fields = ('output',)