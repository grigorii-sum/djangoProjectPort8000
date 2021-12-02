from rest_framework import serializers

from .models import IdentifierCode


class IdentifierCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifierCode
        fields = "__all__"

