# Generated by Django 3.0.4 on 2020-04-04 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0018_auto_20200404_1759"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="diabetesinitialreview", name="lifestyle_management",
        ),
        migrations.RemoveField(
            model_name="historicaldiabetesinitialreview", name="lifestyle_management",
        ),
        migrations.RemoveField(
            model_name="historicalhivinitialreview", name="lifestyle_management",
        ),
        migrations.RemoveField(
            model_name="historicalhypertensioninitialreview",
            name="lifestyle_management",
        ),
        migrations.RemoveField(
            model_name="hivinitialreview", name="lifestyle_management",
        ),
        migrations.RemoveField(
            model_name="hypertensioninitialreview", name="lifestyle_management",
        ),
    ]
