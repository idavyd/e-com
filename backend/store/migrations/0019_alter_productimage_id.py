# Generated by Django 5.1.4 on 2025-01-29 09:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_rename_product_id_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
