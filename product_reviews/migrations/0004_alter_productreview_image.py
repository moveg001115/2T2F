# Generated by Django 4.2.6 on 2023-10-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_reviews', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]