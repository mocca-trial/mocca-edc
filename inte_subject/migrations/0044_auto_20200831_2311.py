# Generated by Django 3.0.9 on 2020-08-31 20:11

from django.db import migrations


def update_subjectvisit(apps, schema_editor):
    subject_visit_model_cls = apps.get_model("inte_subject.subjectvisit")
    for obj in subject_visit_model_cls.objects.all():
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0043_auto_20200826_2148"),
    ]

    operations = [migrations.RunPython(update_subjectvisit)]
