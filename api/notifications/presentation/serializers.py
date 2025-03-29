from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
