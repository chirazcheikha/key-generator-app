from rest_framework import serializers
from crud.models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('key_name','key_description','key','date')