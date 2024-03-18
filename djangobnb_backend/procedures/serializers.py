from rest_framework import serializers

from .models import Procedures

class ProceduresListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Procedures
        fields = (
            'id',
            'title',
            'price_per_procedure',
            'image_url',

        )