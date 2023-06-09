# Generated by Django 3.1 on 2023-03-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_auto_20230312_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Capacity1',
            new_name='variety1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Capacity2',
            new_name='variety2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Capacity3',
            new_name='variety3',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Capacity4',
            new_name='variety4',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Capacity5',
            new_name='variety5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.AddField(
            model_name='product',
            name='sale_percent',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='variety1price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='variety2price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='variety3price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='variety4price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='variety5price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
