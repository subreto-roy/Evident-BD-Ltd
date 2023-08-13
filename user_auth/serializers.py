
from rest_framework import serializers
from .models import InputHistory

class InputHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InputHistory
        fields = ('timestamp', 'input_values')
