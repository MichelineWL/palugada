# Generated by Django 5.1.1 on 2024-09-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
