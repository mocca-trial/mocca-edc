# Generated by Django 3.0.9 on 2020-12-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0008_auto_20201204_0312"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmoccaregister",
            name="call",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="Yes", max_length=15
            ),
        ),
        migrations.AddField(
            model_name="moccaregister",
            name="call",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="Yes", max_length=15
            ),
        ),
    ]
