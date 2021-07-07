from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from rest_framework import serializers

class Client(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	dni = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"

class Room(models.Model):
	
	class RoomStyle(models.TextChoices):
		SINGLE = 'SINGLE', ('Single')
		TWIN = 'TWIN', ('Twin')
		DOUBLE = 'DOUBLE', ('Double')
		DELUXE = 'DELUXE', ('Deluxe')

	style = models.CharField(max_length=10, choices=RoomStyle.choices, default=RoomStyle.SINGLE)

	class Meta:
		verbose_name = "Room"
		verbose_name_plural = "Rooms"

	def __str__(self):
		return f'{self.id} - {self.style}'

class Reserve(models.Model):

	class State(models.TextChoices):
		PENDING = 'PENDING', ('Pending')
		PAID = 'PAID', ('Paid')
		ELIMINATED = 'DEL', ('Eliminated')

	class PayMethod(models.TextChoices):
		CASH = 'CASH', ('Cash')
		CREDIT = 'CREDIT', ('Credit')
		DEBIT = 'DEBIT', ('Debit')
		CHECK = 'CHECK', ('Check')
		TRANSFER = 'TRANSFER', ('Transfer')

	bill_date = models.DateField(auto_now_add=True)
	days_reserved = models.IntegerField(editable=False)
	end_date = models.DateField(default=date.today(), validators=[MinValueValidator(date.today())])
	state = models.CharField(max_length=10, choices=State.choices, default=State.PENDING)
	paid_amount = models.DecimalField(max_digits=6, decimal_places=2)
	pay_method = models.CharField(max_length=10, choices=PayMethod.choices, default=PayMethod.CASH)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if self.end_date:
			delta =  self.end_date - date.today()
			self.days_reserved = delta.days
			super(Reserve, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Reserve"
		verbose_name_plural = "Reserves"
