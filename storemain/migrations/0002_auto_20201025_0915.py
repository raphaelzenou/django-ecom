# Generated by Django 3.1.2 on 2020-10-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='billing_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='billing_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='billing_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='billing_postcode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
