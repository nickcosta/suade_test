# Generated by Django 3.2.5 on 2021-07-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics_report', '0002_auto_20210725_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(),
        ),
    ]
