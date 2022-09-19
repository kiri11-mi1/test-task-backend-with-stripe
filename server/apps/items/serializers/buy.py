from rest_framework import serializers


class BuyRetrieveSerializer(serializers.Serializer):
    id = serializers.CharField()
