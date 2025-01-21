from rest_framework import serializers
from .models import PatientData


class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = '__all__'

    def validate_breath_sound_types(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Breath sound types must be an array of strings")
        return value

    def validate_breath_sound_location(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Breath sound location must be an array of strings")
        return value
