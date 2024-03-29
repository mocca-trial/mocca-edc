# Generated by Django 3.1.7 on 2021-03-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0019_auto_20210326_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cholreview',
            name='care_start_date',
        ),
        migrations.RemoveField(
            model_name='cholreview',
            name='dx',
        ),
        migrations.RemoveField(
            model_name='cholreview',
            name='test_date',
        ),
        migrations.RemoveField(
            model_name='historicalcholreview',
            name='care_start_date',
        ),
        migrations.RemoveField(
            model_name='historicalcholreview',
            name='dx',
        ),
        migrations.RemoveField(
            model_name='historicalcholreview',
            name='test_date',
        ),
        migrations.AlterField(
            model_name='cholreview',
            name='managed_by',
            field=models.CharField(choices=[('drugs', 'Oral drugs'), ('diet_lifestyle', 'Diet and lifestyle alone')], default='N/A', max_length=25, verbose_name="How will the patient's High Cholesterol be managed going forward?"),
        ),
        migrations.AlterField(
            model_name='historicalcholreview',
            name='managed_by',
            field=models.CharField(choices=[('drugs', 'Oral drugs'), ('diet_lifestyle', 'Diet and lifestyle alone')], default='N/A', max_length=25, verbose_name="How will the patient's High Cholesterol be managed going forward?"),
        ),
    ]
