# Generated by Django 4.0 on 2022-02-02 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_options_service_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Services'},
        ),
    ]
