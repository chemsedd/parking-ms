from django.db import models

# Create your models here.

CAR_TYPES = (
    ('B', 'Bicycle'),
    ('BS', 'Bus'),
    ('C', 'Car'),
    ('CT', 'Consumer Truck'),
    ('M', 'Motorcycle'),
    ('T', 'Truck'),
    ('ST', 'Semi Truck'),
    ('V', 'Van')
)


class Lot(models.Model):
    class Meta:
        verbose_name = "lot"
        verbose_name_plural = "lots"

    LOT_STATUS = (
        ('E', 'Empty'),
        ('O', 'Occupied'),
        ('OUT', 'Out of service'),
    )

    # Parking lot ID
    _id = models.IntegerField()
    section = models.CharField(max_length=2)
    veh_type = models.CharField(choices=CAR_TYPES, default="C", max_length=20)
    status = models.CharField(choices=LOT_STATUS, default="E", max_length=20)

    def __str__(self):
        return f"""
        ------------------------------
        ID       : {self._id}
        Section  : {self.section}
        Lot type : {self.veh_type}
        Status   : {self.status}
        ------------------------------
        """

    def get_absolute_url(self):
        return reverse("lot_detail", kwargs={"pk": self.pk})


class Vehicle(models.Model):

    class Meta:
        verbose_name = "vehicle"
        verbose_name_plural = "vehicles"

    _id = models.IntegerField()
    _type = models.CharField(choices=CAR_TYPES, max_length=4)
    owner = models.CharField(max_length=70)

    def __str__(self):
        return f"""
        ------------------------------
        ID      : {self._id}
        Type    : {self._type}
        ------------------------------
        """

    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk})
