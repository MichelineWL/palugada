# Generated by Django 5.1.1 on 2024-09-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_images/'),
        ),
    ]