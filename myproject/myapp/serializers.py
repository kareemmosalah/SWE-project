from rest_framework import serializers

class CourtSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    id = serializers.IntegerField()

class ScheduleSerializer(serializers.Serializer):
    time = serializers.CharField(max_length=100)
    event = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)