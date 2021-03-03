from django.db import models

# Create your models here.

class jumiaa(models.Model):
    ekonga_img_link = models.URLField(max_length=200,blank=True)
    ekonga_product_title = models.CharField(max_length=300,blank=True)
    ekonga_product_price = models.CharField(max_length=500,blank=True)
    ekonga_product_link = models.URLField(max_length=200,blank=True)
    jumia_img_link = models.URLField(max_length=200,blank=True)
    jumia_product_title = models.CharField(max_length=300,blank=True)
    jumia_price = models.CharField(max_length= 500, blank=True)
    link = models.URLField(max_length=200,blank=True)
    
    def __str__(self):
        return self.title