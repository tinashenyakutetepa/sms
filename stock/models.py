from django.db import models

# stock models.
class Stock(models.Model):
    item_name = models.CharField(max_length=15,blank=False,null=True)
    Date_arrived = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.item_name