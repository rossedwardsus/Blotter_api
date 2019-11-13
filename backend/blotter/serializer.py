#from django.contrib.auth.models import User, Group
from .models import BlotterModel
from rest_framework import serializers

class BlotterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlotterModel
        #fields = ['url', 'username', 'email', 'groups']
        fields = "__all__"


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return BlotterModel.objects.create(**validated_data)
        #return