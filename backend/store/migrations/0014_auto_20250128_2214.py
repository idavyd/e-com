from uuid import uuid4
from django.db import migrations

def set_product_ids(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    for product in Product.objects.all():
        product.product_id = uuid4()  # Assign a new UUID
        product.save()

class Migration(migrations.Migration):
    dependencies = [
        ('store', '0013_product_product_id'),  # Replace with the name of the migration before this one
    ]

    operations = [
        migrations.RunPython(set_product_ids),
    ]
