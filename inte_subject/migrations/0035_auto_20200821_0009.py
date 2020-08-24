# Generated by Django 3.0.9 on 2020-08-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0034_auto_20200820_2314"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="diabetes_tested_date",
            new_name="diabetic_tested_date",
        ),
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="diabetes_tested_estimated_datetime",
            new_name="diabetic_tested_estimated_datetime",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="diabetes_tested_date",
            new_name="diabetic_tested_date",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="diabetes_tested_estimated_datetime",
            new_name="diabetic_tested_estimated_datetime",
        ),
    ]
