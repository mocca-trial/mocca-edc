# Generated by Django 3.0.9 on 2020-12-16 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_subject", "0004_remove_reasonforvisit_health_services"),
        ("mocca_lists", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="HealthServices",
        ),
    ]
