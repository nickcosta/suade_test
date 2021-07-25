# Generated by Django 3.2.5 on 2021-07-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics_report', '0004_auto_20210725_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product',
        ),
        migrations.AddField(
            model_name='orderline',
            name='order_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderline',
            name='product_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
