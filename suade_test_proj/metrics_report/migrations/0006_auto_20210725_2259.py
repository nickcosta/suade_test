# Generated by Django 3.2.5 on 2021-07-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics_report', '0005_auto_20210725_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='dicounted_amount',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='full_price_amount',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]
