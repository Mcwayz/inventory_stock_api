from django.db.models import Sum
from django.shortcuts import render, redirect
from base.models import Products, Inventory, Dispatched

# Create your views here.

def index(request):
    # Variables
    dispatched_stock = Dispatched.objects.aggregate(Sum('dispatch_quantity'))['dispatch_quantity__sum'] or 0
    warehouse_stock = Inventory.objects.aggregate(Sum('product_quantity'))['product_quantity__sum'] or 0
    amigo_products = Products.objects.filter(section__section='Amigo').count()
    sobi_products = Products.objects.filter(section__section='Sobi').count()

    # Pass the data to the template context
    
    context = {
        'dispatched_stock': dispatched_stock,
        'warehouse_stock': warehouse_stock,
        'amigo_products': amigo_products,
        'sobi_products': sobi_products,
    }

    return render(request, 'dashboard/index.html', context)


# Add Products

def AddProducts(request):
    
    if request.method == 'POST':
        section = request.POST.get('section')
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_unit_barcode_no = request.POST.get('product_unit_barcode_no')
        outer_product_case_barcode = request.POST.get('outer_product_case_barcode')

        # Create a new instance of the Products model and populate it with the form data
        new_product = Products(
            section=section,
            product_name=product_name,
            product_desc=product_desc,
            product_unit_barcode_no=product_unit_barcode_no,
            outer_product_case_barcode=outer_product_case_barcode
        )

        # Save the new product to the database
        new_product.save()
    return render(request, 'dashboard/pages/forms/basic_elements.html')



# View Products

def ViewProducts(request):
    products = Products.objects.all()
    
        # Pass the data to the template context
        
    context = {
        'products': products, 
    }
    
    return render(request, 'dashboard/pages/tables/basic-table.html', context)