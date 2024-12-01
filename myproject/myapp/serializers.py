from rest_framework import serializers

class CourtSerializer(serializers.Serializer):
    """
    Serializer for the Court model.
    Serializes the name and id fields of the Court model.
    """
    name = serializers.CharField(max_length=100)  # Name of the court
    id = serializers.IntegerField()  # ID of the court

class ScheduleSerializer(serializers.Serializer):
    """
    Serializer for the Schedule model.
    Serializes the time, event, and status fields of the Schedule model.
    """
    time = serializers.CharField(max_length=100)  # Time slot for the schedule
    event = serializers.CharField(max_length=100)  # Event name for the schedule
    status = serializers.CharField(max_length=100)  # Status of the schedule (e.g., Available, Booked)