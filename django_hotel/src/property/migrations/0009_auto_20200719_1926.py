# Generated by Django 3.0.4 on 2020-07-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200716_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=20),
        ),
    ]