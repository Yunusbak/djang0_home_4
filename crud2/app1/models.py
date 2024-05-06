from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=250)
    company = models.CharField(max_length=150)
    year = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="cars", blank=True, null=True)

    class Meta:
        db_table = "Cars"


    def __str__(self):
        return self.name

    