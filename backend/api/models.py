from django.db import models

# Create your models here.


class Lot(models.Model):

    class Meta:
        verbose_name = "lot"
        verbose_name_plural = "lots"

    LOT_TYPES = (
        ('B', 'Bicycle'),
        ('BS', 'Bus'),
        ('C', 'Car'),
        ('CT', 'Consumer Truck'),
        ('M', 'Motorcycle'),
        ('T', 'Truck'),
        ('ST', 'Semi Truck'),
        ('V', 'Van')
    )

    LOT_STATUS = (
        ('E', 'Empty'),
        ('O', 'Occupied'),
        ('OUT', 'Out of service'),
    )

    # Parking lot ID
    _id = models.IntegerField()
    section = models.CharField(max_length=2)
    veh_type = models.CharField(choices=LOT_TYPES, default="C", max_length=20)
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
