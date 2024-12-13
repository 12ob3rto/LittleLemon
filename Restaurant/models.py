from django.db import models


class BookingTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    numberGuest = models.IntegerField()
    bookingDate = models.DateTimeField(db_index=True)

class MenuTable(models.Model):
    id = models.IntegerField(primary_key=True)
    tittle = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()


