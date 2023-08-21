from django.db import models

# Create your models here.
class Product(models.Model) : 
    title = models.CharField(max_length=120) # have to use max length for a CharField
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    summary = models.TextField(blank=False, null=False) # Blank how it is rendered, Null if null is allowed in the database
    featured = models.BooleanField() # null=True, default=true