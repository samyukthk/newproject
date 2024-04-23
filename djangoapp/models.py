from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField( max_length=50)
    desc=models.CharField( max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product-image', null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    product_details = models.CharField(max_length=1000, null=True, blank=True)
    hide = models.BooleanField(default=False)
    


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   

    # name = models.CharField(max_length=50, null=True, blank=True)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # offer_percentage = models.FloatField(null=True, blank=True)
    # availability = models.BooleanField(default=True)
    # hide = models.BooleanField(default=False)
    
    
class ImageTest(models.Model):
    imagename=models.CharField( max_length=50)
    image=models.ImageField(upload_to='Image')