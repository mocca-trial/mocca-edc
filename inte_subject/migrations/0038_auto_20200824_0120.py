# Generated by Django 3.0.9 on 2020-08-23 22:20

from django.db import migrations, models
import edc_model.models.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0037_auto_20200823_2223"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="hiv_result",
            new_name="hiv_tested",
        ),
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="hiv_result_ago",
            new_name="hiv_tested_ago",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="hiv_result_ago",
            new_name="hiv_tested_ago",
        ),
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="hiv_result_date",
            new_name="hiv_tested_date",
        ),
        migrations.RenameField(
            model_name="clinicalreviewbaseline",
            old_name="hiv_result_estimated_datetime",
            new_name="hiv_tested_estimated_datetime",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="hiv_result",
            new_name="hiv_tested",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="hiv_result_date",
            new_name="hiv_tested_date",
        ),
        migrations.RenameField(
            model_name="historicalclinicalreviewbaseline",
            old_name="hiv_result_estimated_datetime",
            new_name="hiv_tested_estimated_datetime",
        ),
        migrations.AlterField(
            model_name="clinicalreviewbaseline",
            name="diabetes_tested_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
            ),
        ),
        migrations.AlterField(
            model_name="clinicalreviewbaseline",
            name="hypertension_tested_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
            ),
        ),
        migrations.AlterField(
            model_name="historicalclinicalreviewbaseline",
            name="diabetes_tested_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
            ),
        ),
        migrations.AlterField(
            model_name="historicalclinicalreviewbaseline",
            name="hypertension_tested_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
            ),
        ),
    ]
