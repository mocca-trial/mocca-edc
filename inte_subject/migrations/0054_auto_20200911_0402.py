# Generated by Django 3.0.9 on 2020-09-11 01:02

from django.db import migrations
from django.db.models.signals import pre_save
from edc_utils import DisableSignals


class Migration(migrations.Migration):
    def update_visit_code_and_sequence(apps, schema_editor):
        subject_visit_model_cls = apps.get_model("inte_subject.subjectvisit")
        for subject_visit in subject_visit_model_cls.objects.all():
            with DisableSignals(disabled_signals=[pre_save]):
                subject_visit.visit_code = subject_visit.appointment.visit_code
                subject_visit.visit_code_sequence = (
                    subject_visit.appointment.visit_code_sequence
                )
                subject_visit.save()

    dependencies = [
        ("inte_subject", "0053_auto_20200910_2201"),
    ]

    operations = [migrations.RunPython(update_visit_code_and_sequence)]