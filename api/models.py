from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=100,null=False,blank=False)
    desc = models.TextField()
    stars = models.IntegerField()
    
    def __str__(self):
        return self.name
   