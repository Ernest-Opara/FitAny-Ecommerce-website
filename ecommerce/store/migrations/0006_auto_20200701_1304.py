# Generated by Django 3.0.7 on 2020-07-01 12:04

from django.db import migrations, models
import uuid
from store.models import Product  

def gen_uuid(apps, schema_editor):
    product = apps.get_model('store', 'Product')
    for row in product.objects.all():
        row.slug = uuid.uuid4()
        row.save(update_fields=['slug'])

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200701_1301'),
    ]

    operations = [
       migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]





   

    