# Generated by Django 3.0.9 on 2020-09-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0007_auto_20200910_1742"),
        ("inte_subject", "0051_auto_20200910_2111"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinicalreviewbaseline",
            name="hiv_dx",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If yes, complete form `HIV Initial Review`",
                max_length=15,
                verbose_name="Has the patient ever tested positive for HIV?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalclinicalreviewbaseline",
            name="hiv_dx",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If yes, complete form `HIV Initial Review`",
                max_length=15,
                verbose_name="Has the patient ever tested positive for HIV?",
            ),
        ),
    ]