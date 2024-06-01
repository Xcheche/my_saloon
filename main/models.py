from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Story(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='salon/images/')
    price= models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name
    

class Barber(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='salon/barbers/')

    def __str__(self):
        return self.name
    
class ServicePrice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, null=True, blank=True)
    price= models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.service.name} - {"No Barber Assigned" if not self.barber else self.barber.name}:${self.price}'

    

class  Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'Booking by {self.name} for {self.service.name}'

