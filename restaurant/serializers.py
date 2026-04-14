from rest_framework import serializers
from .models import Menu, Booking
from django.utils import timezone

class MenuSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description']

        def __str__(self):
            return self.name

class BookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Booking
        fields = ['id', 'first_name', 'reservation_date', 'reservation_slot', 'party_size']
        
    def __str__(self):
        return self.first_name

    def validate_reservation_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Reservation date cannot be in the past")
        return value

    def validate(self, data):
        # Check if this time slot is already booked
        existing = Booking.objects.filter(
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot']
        ).exists()
        
        if existing:
            raise serializers.ValidationError(
                "This time slot is already booked. Please choose another."
            )
        return data
