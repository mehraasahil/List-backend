from rest_framework import serializers
from.models import  Employement

class EmployementSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Employement
        fields = '__all__'



