# Generated by Django 3.0.5 on 2020-04-04 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0015_auto_20200311_1613"),
    ]

    operations = [
        migrations.RemoveField(model_name="anthropometry", name="waist_circumference",),
        migrations.RemoveField(
            model_name="historicalanthropometry", name="waist_circumference",
        ),
    ]