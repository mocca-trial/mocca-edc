# Generated by Django 3.1.6 on 2021-03-02 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0016_auto_20210302_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugrefillhiv',
            name='clinic_days',
        ),
        migrations.RemoveField(
            model_name='drugrefillhiv',
            name='club_days',
        ),
        migrations.RemoveField(
            model_name='drugrefillhiv',
            name='purchased_days',
        ),
        migrations.RemoveField(
            model_name='historicaldrugrefillhiv',
            name='clinic_days',
        ),
        migrations.RemoveField(
            model_name='historicaldrugrefillhiv',
            name='club_days',
        ),
        migrations.RemoveField(
            model_name='historicaldrugrefillhiv',
            name='purchased_days',
        ),
    ]
