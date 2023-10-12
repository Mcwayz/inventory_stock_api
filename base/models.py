from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# Product Sections
class ProductSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    section = models.CharField(max_length=100)
    section_desc = models.TextField(max_length=200)
    
    
# Products
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField(max_length=150)
    product_desc = models.TextField(max_length=200)
    product_unit_barcode_no = models.CharField(max_length=200)
    outer_product_case_barcode = models.CharField(max_length=200)
    section = models.ForeignKey(ProductSection, on_delete=models.CASCADE, related_name='product_section')
 
    
# Product Stock 
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product_quantity = models.IntegerField(max_length=100)
    product_last_action = models.CharField(max_length=200) 
    product_last_update = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_inventory')
    

