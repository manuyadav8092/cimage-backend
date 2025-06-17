from rest_framework import serializers

class userDetailsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email =serializers.EmailField()
    mobile =serializers.CharField(max_length=50)
    address =serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)