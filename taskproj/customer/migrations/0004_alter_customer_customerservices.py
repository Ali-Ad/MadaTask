# Generated by Django 4.0 on 2022-01-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('customer', '0003_remove_customer_customerservices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerservices',
            field=models.ManyToManyField(to='service.Service'),
        ),
    ]
