# Generated by Django 3.0.6 on 2020-08-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0029_auto_20200813_1817"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healtheconomics",
            name="childcare_source",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("working", "Working"),
                    ("studying", "Studying"),
                    ("caring_for_children", "Caring for children"),
                    ("house_maintenance", "House maintenance"),
                    ("nothing", "Nothing"),
                    ("OTHER", "Other, specify"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If Yes, what would they have been doing if they had not stayed to look after your child or children?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicsrevised",
            name="childcare_source",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("working", "Working"),
                    ("studying", "Studying"),
                    ("caring_for_children", "Caring for children"),
                    ("house_maintenance", "House maintenance"),
                    ("nothing", "Nothing"),
                    ("OTHER", "Other, specify"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If Yes, what would they have been doing if they had not stayed to look after your child or children?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomics",
            name="childcare_source",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("working", "Working"),
                    ("studying", "Studying"),
                    ("caring_for_children", "Caring for children"),
                    ("house_maintenance", "House maintenance"),
                    ("nothing", "Nothing"),
                    ("OTHER", "Other, specify"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If Yes, what would they have been doing if they had not stayed to look after your child or children?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicsrevised",
            name="childcare_source",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("working", "Working"),
                    ("studying", "Studying"),
                    ("caring_for_children", "Caring for children"),
                    ("house_maintenance", "House maintenance"),
                    ("nothing", "Nothing"),
                    ("OTHER", "Other, specify"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="If Yes, what would they have been doing if they had not stayed to look after your child or children?",
            ),
        ),
    ]
