# Generated by Django 3.0.9 on 2020-09-26 20:04

from django.db import migrations
import edc_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0064_auto_20200926_2257"),
    ]

    operations = [
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_other_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_other_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
    ]
