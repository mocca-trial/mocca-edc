# Generated by Django 3.0.4 on 2020-04-04 14:59

from django.db import migrations
import edc_model.models.fields.date_estimated


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0017_auto_20200404_1744"),
    ]

    operations = [
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
        migrations.AddField(
            model_name="historicalhivinitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
        migrations.AddField(
            model_name="historicalhypertensioninitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
        migrations.AddField(
            model_name="hivinitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
        migrations.AddField(
            model_name="hypertensioninitialreview",
            name="diagnosis_date_estimated",
            field=edc_model.models.fields.date_estimated.IsDateEstimatedFieldNa(
                blank=True,
                choices=[
                    ("N/A", "Not applicable"),
                    ("not_estimated", "No."),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                default="not_estimated",
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is the dignosis date estimated",
            ),
        ),
    ]
