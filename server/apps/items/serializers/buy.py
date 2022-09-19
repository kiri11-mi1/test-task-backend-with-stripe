from rest_framework import serializers


class BuyRetrieveSerializer(serializers.Serializer):
    stripe_session_id = serializers.CharField()
