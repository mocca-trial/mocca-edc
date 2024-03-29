# Generated by Django 3.1.6 on 2021-03-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0014_auto_20210301_0507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodresultsfbc',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'), 'get_latest_by': 'modified', 'ordering': ('-modified', '-created'), 'verbose_name': 'Blood Result: FBC', 'verbose_name_plural': 'Blood Results: FBC'},
        ),
        migrations.AlterModelOptions(
            name='historicalbloodresultsfbc',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Blood Result: FBC'},
        ),
        migrations.RemoveField(
            model_name='clinicalreviewbaseline',
            name='chol_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='clinicalreviewbaseline',
            name='dm_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='clinicalreviewbaseline',
            name='hiv_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='clinicalreviewbaseline',
            name='htn_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalclinicalreviewbaseline',
            name='chol_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalclinicalreviewbaseline',
            name='dm_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalclinicalreviewbaseline',
            name='hiv_test_estimated_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalclinicalreviewbaseline',
            name='htn_test_estimated_datetime',
        ),
        migrations.AddField(
            model_name='clinicalreviewbaseline',
            name='chol_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `chol_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='clinicalreviewbaseline',
            name='dm_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `dm_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='clinicalreviewbaseline',
            name='hiv_test_estimated_date',
            field=models.DateField(blank=True, editable=False, help_text='calculated by the EDC using `hiv_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='clinicalreviewbaseline',
            name='htn_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `htn_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='historicalclinicalreviewbaseline',
            name='chol_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `chol_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='historicalclinicalreviewbaseline',
            name='dm_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `dm_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='historicalclinicalreviewbaseline',
            name='hiv_test_estimated_date',
            field=models.DateField(blank=True, editable=False, help_text='calculated by the EDC using `hiv_test_ago`', null=True),
        ),
        migrations.AddField(
            model_name='historicalclinicalreviewbaseline',
            name='htn_test_estimated_date',
            field=models.DateField(blank=True, help_text='calculated by the EDC using `htn_test_ago`', null=True),
        ),
    ]
