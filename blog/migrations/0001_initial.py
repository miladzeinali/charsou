# Generated by Django 4.1.7 on 2023-03-17 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog-main/')),
                ('summary', models.TextField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, max_length=1500, null=True)),
                ('writer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.writer')),
            ],
        ),
    ]