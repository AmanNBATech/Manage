from rest_framework import serializers
from .models import *


class aman(serializers.ModelSerializer):
    class Meta:
        model = add
        fields ='__all__'
