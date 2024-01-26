from django.db import models

# Create your models here.
class Product(models.Model): 
    product_id = models.AutoField(primary_key=True) #primary key
    product_name = models.CharField(max_length=100) #character varying 100
    product_description = models.TextField()
    product_price = models.IntegerField ()

    def __str__(self):
        return self.product_name +" -- "+ self.product_description

class ProductCategory (models.Model):
    p_cat_name = models.CharField(max_length = 100)
    p_cat_desc = models.TextField()
    p_cat_image = models.ImageField(null=True, blank=True, upload_to='images/')
    