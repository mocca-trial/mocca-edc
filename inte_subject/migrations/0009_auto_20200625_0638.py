# Generated by Django 3.0.6 on 2020-06-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0002_auto_20200625_0329"),
        ("inte_subject", "0008_auto_20200625_0329"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drugrefilldiabetes",
            name="modifications",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModifications",
                verbose_name="Which changes occurred?",
            ),
        ),
        migrations.AlterField(
            model_name="drugrefilldiabetes",
            name="modifications_reason",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModificationReasons",
                verbose_name="Why did the patient’s previous prescription change?",
            ),
        ),
        migrations.AlterField(
            model_name="drugrefillhiv",
            name="modifications",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModifications",
                verbose_name="Which changes occurred?",
            ),
        ),
        migrations.AlterField(
            model_name="drugrefillhiv",
            name="modifications_reason",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModificationReasons",
                verbose_name="Why did the patient’s previous prescription change?",
            ),
        ),
        migrations.AlterField(
            model_name="drugrefillhypertension",
            name="modifications",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModifications",
                verbose_name="Which changes occurred?",
            ),
        ),
        migrations.AlterField(
            model_name="drugrefillhypertension",
            name="modifications_reason",
            field=models.ManyToManyField(
                blank=True,
                to="inte_lists.RxModificationReasons",
                verbose_name="Why did the patient’s previous prescription change?",
            ),
        ),
    ]
