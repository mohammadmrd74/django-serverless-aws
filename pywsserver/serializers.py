from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    deviceModel = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    note = serializers.CharField(max_length=400)
    serial = serializers.CharField(max_length=100)
