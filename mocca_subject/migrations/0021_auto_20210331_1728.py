# Generated by Django 3.1.7 on 2021-03-31 14:28

from django.db import migrations, models
import django.db.models.deletion
import edc_model.models.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0020_auto_20210326_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glucose',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'), 'get_latest_by': 'modified', 'ordering': ('-modified', '-created'), 'verbose_name': 'Glucose: Followup', 'verbose_name_plural': 'Glucose: Followup'},
        ),
        migrations.AlterModelOptions(
            name='historicalglucose',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Glucose: Followup'},
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='care_start_date',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='dx',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='glucose',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='glucose_date',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='glucose_fasted',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='glucose_quantifier',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='glucose_units',
        ),
        migrations.RemoveField(
            model_name='dmreview',
            name='test_date',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='care_start_date',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='dx',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='glucose',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='glucose_date',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='glucose_fasted',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='glucose_quantifier',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='glucose_units',
        ),
        migrations.RemoveField(
            model_name='historicaldmreview',
            name='test_date',
        ),
        migrations.AddField(
            model_name='clinicalreviewbaseline',
            name='complications',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='-', help_text='If Yes, complete the `Complications` CRF', max_length=15, verbose_name='Since last seen, has the patient had any complications'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glucose',
            name='fasting',
            field=models.CharField(blank=True, choices=[('fasting', 'Fasting'), ('non_fasting', 'Non-fasting')], max_length=25, null=True, verbose_name='Was this fasting or non-fasting?'),
        ),
        migrations.AddField(
            model_name='glucose',
            name='glucose_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='glucose',
            name='glucose_assay_datetime',
            field=models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time'),
        ),
        migrations.AddField(
            model_name='glucose',
            name='glucose_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='glucose',
            name='glucose_requisition',
            field=models.ForeignKey(blank=True, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bg', to='mocca_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='glucose',
            name='is_poc',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True, verbose_name='Was a point-of-care test used?'),
        ),
        migrations.AddField(
            model_name='historicalclinicalreviewbaseline',
            name='complications',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='-', help_text='If Yes, complete the `Complications` CRF', max_length=15, verbose_name='Since last seen, has the patient had any complications'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='fasting',
            field=models.CharField(blank=True, choices=[('fasting', 'Fasting'), ('non_fasting', 'Non-fasting')], max_length=25, null=True, verbose_name='Was this fasting or non-fasting?'),
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='glucose_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='glucose_assay_datetime',
            field=models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time'),
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='glucose_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='glucose_requisition',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='historicalglucose',
            name='is_poc',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True, verbose_name='Was a point-of-care test used?'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='fasting',
            field=models.CharField(blank=True, choices=[('fasting', 'Fasting'), ('non_fasting', 'Non-fasting')], max_length=25, null=True, verbose_name='Was this fasting or non-fasting?'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='glucose_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='glucose_assay_datetime',
            field=models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='glucose_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='glucose_requisition',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='historicalglucosebaseline',
            name='is_poc',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True, verbose_name='Was a point-of-care test used?'),
        ),
    ]
