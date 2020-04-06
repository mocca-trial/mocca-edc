# Generated by Django 3.0.4 on 2020-04-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0022_auto_20200404_1918"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="diabetesinitialreview", name="glucose_datetime",
        ),
        migrations.RemoveField(
            model_name="historicaldiabetesinitialreview", name="glucose_datetime",
        ),
        migrations.AlterField(
            model_name="diabetesinitialreview",
            name="fasted",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AlterField(
            model_name="diabetesinitialreview",
            name="glucose_measurement_reason_not_taken",
            field=models.TextField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="If the glucose measurement was not taken, explain?",
            ),
        ),
        migrations.AlterField(
            model_name="diabetesinitialreview",
            name="glucose_units",
            field=models.CharField(
                choices=[
                    ("mg/dL", "mg/dL"),
                    ("mmol/L", "mmol/L"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=15,
                verbose_name="Units (glucose)",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiabetesinitialreview",
            name="fasted",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiabetesinitialreview",
            name="glucose_measurement_reason_not_taken",
            field=models.TextField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="If the glucose measurement was not taken, explain?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiabetesinitialreview",
            name="glucose_units",
            field=models.CharField(
                choices=[
                    ("mg/dL", "mg/dL"),
                    ("mmol/L", "mmol/L"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=15,
                verbose_name="Units (glucose)",
            ),
        ),
    ]
