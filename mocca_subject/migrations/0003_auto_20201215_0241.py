# Generated by Django 3.0.9 on 2020-12-14 23:41

from django.db import migrations, models
import edc_model.models.fields.duration
import edc_model.models.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_subject", "0002_remove_subjectvisit_health_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="clinicalreviewbaseline",
            name="chol_dx",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If yes, complete form `High Cholesterol Initial Review`",
                max_length=15,
                verbose_name="Have you ever been diagnosed with High Cholesterol",
            ),
        ),
        migrations.AddField(
            model_name="clinicalreviewbaseline",
            name="chol_test",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="-",
                max_length=15,
                verbose_name="Has the patient ever tested for High Cholesterol?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clinicalreviewbaseline",
            name="chol_test_ago",
            field=edc_model.models.fields.duration.DurationYMDField(
                blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="clinicalreviewbaseline",
            name="chol_test_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
                verbose_name="Date of patient's most recent Cholesterol test?",
            ),
        ),
        migrations.AddField(
            model_name="clinicalreviewbaseline",
            name="chol_test_estimated_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="calculated by the EDC using `chol_test_ago`",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalclinicalreviewbaseline",
            name="chol_dx",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If yes, complete form `High Cholesterol Initial Review`",
                max_length=15,
                verbose_name="Have you ever been diagnosed with High Cholesterol",
            ),
        ),
        migrations.AddField(
            model_name="historicalclinicalreviewbaseline",
            name="chol_test",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="-",
                max_length=15,
                verbose_name="Has the patient ever tested for High Cholesterol?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalclinicalreviewbaseline",
            name="chol_test_ago",
            field=edc_model.models.fields.duration.DurationYMDField(
                blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalclinicalreviewbaseline",
            name="chol_test_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
                verbose_name="Date of patient's most recent Cholesterol test?",
            ),
        ),
        migrations.AddField(
            model_name="historicalclinicalreviewbaseline",
            name="chol_test_estimated_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="calculated by the EDC using `chol_test_ago`",
                null=True,
            ),
        ),
    ]
