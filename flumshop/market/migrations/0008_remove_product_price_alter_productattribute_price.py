# Generated by Django 4.1 on 2022-11-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_productattribute_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
