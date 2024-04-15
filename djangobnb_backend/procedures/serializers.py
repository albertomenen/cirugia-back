from rest_framework import serializers

from .models import Procedures, Reservation

from useraccount.serializers import UserDetailsSerializer

class ProceduresListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Procedures
        fields = (
            'id',
            'title',
            'price_per_procedure',
            'image_url',
          

        )
        def get_image_url(self, obj):
            return obj.image_url()

class ProcedureDetailSerializer(serializers.ModelSerializer):
    doctor = UserDetailsSerializer(read_only=True, many=False)
    class Meta:
        model = Procedures
        fields = (
            'id',
            'title',
            'description',
            'price_per_procedure',
            'payment',
            'country',
            'country_code',
            'image',
            'hospitals',
            'information_procedure',
            'doctor',
        )
class ReservationsListSerializer(serializers.ModelSerializer):
    procedures = ProceduresListSerializer(read_only=True, many=False)
    class Meta:
        model = Reservation
        fields = (
            'id', 'start_date', 'total_price', 'procedures', 
        )