# Generated by Django 3.1.6 on 2021-03-01 02:07

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_action_item', '0028_auto_20210203_0706'),
        ('mocca_subject', '0013_auto_20210301_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmreview',
            name='glucose_fasted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Has the participant fasted?'),
        ),
        migrations.AlterField(
            model_name='dmreview',
            name='glucose_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Units (glucose)'),
        ),
        migrations.AlterField(
            model_name='glucose',
            name='glucose_fasted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Has the participant fasted?'),
        ),
        migrations.AlterField(
            model_name='glucose',
            name='glucose_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Units (glucose)'),
        ),
        migrations.AlterField(
            model_name='historicaldmreview',
            name='glucose_fasted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Has the participant fasted?'),
        ),
        migrations.AlterField(
            model_name='historicaldmreview',
            name='glucose_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Units (glucose)'),
        ),
        migrations.AlterField(
            model_name='historicalglucose',
            name='glucose_fasted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Has the participant fasted?'),
        ),
        migrations.AlterField(
            model_name='historicalglucose',
            name='glucose_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Units (glucose)'),
        ),
        migrations.AlterField(
            model_name='historicalglucosebaseline',
            name='glucose_fasted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Has the participant fasted?'),
        ),
        migrations.AlterField(
            model_name='historicalglucosebaseline',
            name='glucose_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)'), ('N/A', 'Not applicable')], default='N/A', max_length=15, verbose_name='Units (glucose)'),
        ),
        migrations.CreateModel(
            name='HistoricalBloodResultsLipid',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.models.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('results_abnormal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?')),
                ('results_reportable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.', max_length=25, verbose_name='If any results are abnormal, are results within grade 3 or above?')),
                ('summary', models.TextField(blank=True, null=True)),
                ('lipid_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time')),
                ('ldl', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='LDL')),
                ('ldl_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('ldl_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('ldl_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('hdl', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='HDL')),
                ('hdl_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('hdl_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('hdl_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('trig', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Triglycerides')),
                ('trig_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('trig_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('trig_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('lipid_requisition', models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectrequisition', verbose_name='Requisition')),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
                ('subject_visit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectvisit')),
            ],
            options={
                'verbose_name': 'historical Blood Result: Lipids',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBloodResultsFbc',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.models.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('results_abnormal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?')),
                ('results_reportable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.', max_length=25, verbose_name='If any results are abnormal, are results within grade 3 or above?')),
                ('summary', models.TextField(blank=True, null=True)),
                ('fbc_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time')),
                ('haemoglobin', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True)),
                ('haemoglobin_units', models.CharField(blank=True, choices=[('g/dL', 'g/dL')], max_length=15, null=True, verbose_name='units')),
                ('haemoglobin_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('haemoglobin_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('hct', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(999.0)], verbose_name='Hematocrit')),
                ('hct_units', models.CharField(blank=True, choices=[('%', '%')], max_length=15, null=True, verbose_name='units')),
                ('hct_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('hct_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('rbc', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(999999.0)], verbose_name='Red blood cell count')),
                ('rbc_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm^3')], max_length=15, null=True, verbose_name='units')),
                ('rbc_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('rbc_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('wbc', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='WBC')),
                ('wbc_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm<sup>3</sup>')], max_length=15, null=True, verbose_name='units')),
                ('wbc_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('wbc_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('platelets', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('platelets_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm<sup>3</sup>')], max_length=15, null=True, verbose_name='units')),
                ('platelets_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('platelets_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('fbc_requisition', models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectrequisition', verbose_name='Requisition')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
                ('subject_visit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mocca_subject.subjectvisit')),
            ],
            options={
                'verbose_name': 'historical blood results fbc',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='BloodResultsLipid',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('tracking_identifier', models.CharField(max_length=30, unique=True)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.models.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('results_abnormal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?')),
                ('results_reportable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.', max_length=25, verbose_name='If any results are abnormal, are results within grade 3 or above?')),
                ('summary', models.TextField(blank=True, null=True)),
                ('lipid_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time')),
                ('ldl', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='LDL')),
                ('ldl_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('ldl_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('ldl_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('hdl', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='HDL')),
                ('hdl_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('hdl_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('hdl_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('trig', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Triglycerides')),
                ('trig_units', models.CharField(blank=True, choices=[('mmol/L', 'mmol/L')], max_length=15, null=True, verbose_name='units')),
                ('trig_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('trig_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.actionitem')),
                ('lipid_requisition', models.ForeignKey(blank=True, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lipid', to='mocca_subject.subjectrequisition', verbose_name='Requisition')),
                ('parent_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
                ('subject_visit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mocca_subject.subjectvisit')),
            ],
            options={
                'verbose_name': 'Blood Result: Lipids',
                'verbose_name_plural': 'Blood Results: Lipids',
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
            managers=[
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
                ('on_site', edc_visit_tracking.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BloodResultsFbc',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('tracking_identifier', models.CharField(max_length=30, unique=True)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_model.models.validators.date.datetime_not_future], verbose_name='Report Date')),
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('results_abnormal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?')),
                ('results_reportable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.', max_length=25, verbose_name='If any results are abnormal, are results within grade 3 or above?')),
                ('summary', models.TextField(blank=True, null=True)),
                ('fbc_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='Result Report Date and Time')),
                ('haemoglobin', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True)),
                ('haemoglobin_units', models.CharField(blank=True, choices=[('g/dL', 'g/dL')], max_length=15, null=True, verbose_name='units')),
                ('haemoglobin_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('haemoglobin_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('hct', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(999.0)], verbose_name='Hematocrit')),
                ('hct_units', models.CharField(blank=True, choices=[('%', '%')], max_length=15, null=True, verbose_name='units')),
                ('hct_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('hct_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('rbc', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(999999.0)], verbose_name='Red blood cell count')),
                ('rbc_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm^3')], max_length=15, null=True, verbose_name='units')),
                ('rbc_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('rbc_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('wbc', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='WBC')),
                ('wbc_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm<sup>3</sup>')], max_length=15, null=True, verbose_name='units')),
                ('wbc_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('wbc_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('platelets', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('platelets_units', models.CharField(blank=True, choices=[('10^9/L', '10^9/L'), ('cells/mm^3', 'cells/mm<sup>3</sup>')], max_length=15, null=True, verbose_name='units')),
                ('platelets_abnormal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal')),
                ('platelets_reportable', models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('3', 'Yes, grade 3'), ('4', 'Yes, grade 4'), ('No', 'Not reportable'), ('Already reported', 'Already reported'), ('present_at_baseline', 'Present at baseline')], max_length=25, null=True, verbose_name='reportable')),
                ('action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.actionitem')),
                ('fbc_requisition', models.ForeignKey(blank=True, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fbc', to='mocca_subject.subjectrequisition', verbose_name='Requisition')),
                ('parent_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
                ('subject_visit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mocca_subject.subjectvisit')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
            managers=[
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
                ('on_site', edc_visit_tracking.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='bloodresultslipid',
            index=models.Index(fields=['subject_visit', 'site', 'id'], name='mocca_subje_subject_f7e032_idx'),
        ),
        migrations.AddIndex(
            model_name='bloodresultsfbc',
            index=models.Index(fields=['subject_visit', 'site', 'id'], name='mocca_subje_subject_6029f5_idx'),
        ),
    ]