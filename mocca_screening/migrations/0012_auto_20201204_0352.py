# Generated by Django 3.0.9 on 2020-12-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0011_auto_20201204_0347"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmoccaregister",
            name="date_last_called",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="moccaregister",
            name="date_last_called",
            field=models.DateField(null=True),
        ),
    ]
