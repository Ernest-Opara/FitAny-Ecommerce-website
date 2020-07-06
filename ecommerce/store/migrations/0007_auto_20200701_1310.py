# Generated by Django 3.0.7 on 2020-07-01 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200701_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]