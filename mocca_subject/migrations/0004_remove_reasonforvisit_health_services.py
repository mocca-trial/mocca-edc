# Generated by Django 3.0.9 on 2020-12-16 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_subject", "0003_auto_20201215_0241"),
    ]

    operations = [
        migrations.RemoveField(model_name="reasonforvisit", name="health_services",),
    ]