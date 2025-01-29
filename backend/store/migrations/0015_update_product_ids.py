from django.db import migrations
from uuid import uuid4

def set_product_ids(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    for product in Product.objects.all():
        # Replace the product_id for all products
        product.product_id = uuid4()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20250128_2214'),  # Adjust this to your last migration
    ]

    operations = [
        migrations.RunPython(set_product_ids),
    ]
