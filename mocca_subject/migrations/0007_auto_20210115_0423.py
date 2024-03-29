# Generated by Django 3.0.9 on 2021-01-15 01:23

import edc_model.models.fields.other_charfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_subject", "0006_auto_20210115_0411"),
    ]

    operations = [
        migrations.AddField(
            model_name="dminitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicaldminitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhivinitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhtninitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="hivinitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="htninitialreview",
            name="dx_location_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="dminitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldminitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhivinitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhtninitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
        migrations.AlterField(
            model_name="hivinitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
        migrations.AlterField(
            model_name="htninitialreview",
            name="dx_location",
            field=models.CharField(
                choices=[
                    ("hospital", "Hospital"),
                    ("gov_clinic", "Government clinic"),
                    ("private_clinic", "Private clinic"),
                    ("private_doctor", "Private doctor"),
                    ("mocca_clinic", "MOCCA study clinic"),
                    ("unknown", "Don't recall"),
                    ("OTHER", "Other, specify"),
                ],
                max_length=25,
                verbose_name="Where was the diagnosis made?",
            ),
        ),
    ]
