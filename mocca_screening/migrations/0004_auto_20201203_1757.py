# Generated by Django 3.0.9 on 2020-12-03 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0003_auto_20201203_1610"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmoccaregister",
            name="screening_identifier",
            field=models.CharField(
                max_length=15,
                null=True,
                verbose_name="MOCCA (ext) screening identifier",
            ),
        ),
        migrations.AddField(
            model_name="moccaregister",
            name="screening_identifier",
            field=models.CharField(
                max_length=15,
                null=True,
                verbose_name="MOCCA (ext) screening identifier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="mocca_register",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                limit_choices_to={"screening_identifier__isnull": True},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="mocca_screening.MoccaRegister",
                verbose_name="Select one from the MOCCA (original) register",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="mocca_register",
            field=models.OneToOneField(
                limit_choices_to={"screening_identifier__isnull": True},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="mocca_screening.MoccaRegister",
                verbose_name="Select one from the MOCCA (original) register",
            ),
        ),
    ]
