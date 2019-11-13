#from django.contrib.auth.models import User, Group
#from .models import Blotter
from rest_framework import serializers

class BlotterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blotter
        #fields = ['url', 'username', 'email', 'groups']
        fields = __all__
