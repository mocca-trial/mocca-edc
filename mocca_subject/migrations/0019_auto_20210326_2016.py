# Generated by Django 3.1.7 on 2021-03-26 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0018_auto_20210302_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='action_item',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='fbc_requisition',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='parent_action_item',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='related_action_item',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='site',
        ),
        migrations.RemoveField(
            model_name='historicalbloodresultsfbc',
            name='subject_visit',
        ),
        migrations.AddField(
            model_name='bloodresultslipid',
            name='chol',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Cholesterol'),
        ),
        migrations.AddField(
            model_name='bloodresultslipid',
            name='chol_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='bloodresultslipid',
            name='chol_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='bloodresultslipid',
            name='chol_units',
            field=models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultslipid',
            name='chol',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Cholesterol'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultslipid',
            name='chol_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultslipid',
            name='chol_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='historicalbloodresultslipid',
            name='chol_units',
            field=models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units'),
        ),
        migrations.DeleteModel(
            name='BloodResultsFbc',
        ),
        migrations.DeleteModel(
            name='HistoricalBloodResultsFbc',
        ),
    ]
