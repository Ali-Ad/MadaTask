# Generated by Django 4.0 on 2022-01-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('customer', '0002_customer_customerservices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customerservices',
        ),
        migrations.AddField(
            model_name='customer',
            name='customerservices',
            field=models.ManyToManyField(default=None, to='service.Service'),
        ),
    ]
