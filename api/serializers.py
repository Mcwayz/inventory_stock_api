from rest_framework import serializers
from base.models import Products, ProductSection, Inventory


# Product Section Serializer
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSection
        fields = ('section_id', 'section', 'section_desc')
        
        
# Product Serializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id', 'product_name', 'product_desc', 'product_unit_barcode_no','outer_product_case_barcode','section')
        

# Inventory Serializer

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('inventory_id', 'product_name', 'product_quantity', 'product_last_action','product_last_update','section')