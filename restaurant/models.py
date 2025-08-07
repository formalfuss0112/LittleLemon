from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
 

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    number_of_guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.price:.2f}'  # Always show 2 decimal places
