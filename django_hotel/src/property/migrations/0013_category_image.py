# Generated by Django 3.0.4 on 2020-07-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
    ]
