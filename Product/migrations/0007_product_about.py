# Generated by Django 4.1.6 on 2023-03-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_remove_product_capacity_product_capacity1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
