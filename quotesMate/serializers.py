from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Quotelist

class QuoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Quotelist
        fields='__all__'