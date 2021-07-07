from .models import Client, Room, Reserve
from rest_framework import serializers

class ClientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Room
		fields = '__all__'

class ReserveSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Reserve
		fields = ['client', 'room', 'end_date', 'days_reserved', 'state', 'paid_amount', 'pay_method']