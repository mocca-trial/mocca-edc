# Generated by Django 3.0.9 on 2020-12-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0016_auto_20201204_2347"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalmoccaregistercontact",
            name="answered",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], max_length=15, null=True
            ),
        ),
        migrations.AlterField(
            model_name="moccaregistercontact",
            name="answered",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], max_length=15, null=True
            ),
        ),
    ]
