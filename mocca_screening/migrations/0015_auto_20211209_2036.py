# Generated by Django 3.2.10 on 2021-12-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_screening', '0014_auto_20210413_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectscreening',
            name='real_eligibility_datetime',
            field=models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to now', null=True),
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='real_eligibility_datetime',
            field=models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to now', null=True),
        ),
        migrations.AlterField(
            model_name='carestatus',
            name='icc_not_in_reason',
            field=models.CharField(choices=[('icc_not_available', 'ICC not available (or closed) in this facility'), ('moved', 'Moved out of area'), ('dont_want', 'Personally chose not to continue with integrated care'), ('advised_to_vertical', 'Healthcare staff asked patient to return to vertical care'), ('referred_out', 'Referred to another facility without an ICC'), ('receives_community_care', 'Patient is currently receiving their HIV care in the community'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If not receiving integrated care, why not?'),
        ),
        migrations.AlterField(
            model_name='historicalcarestatus',
            name='icc_not_in_reason',
            field=models.CharField(choices=[('icc_not_available', 'ICC not available (or closed) in this facility'), ('moved', 'Moved out of area'), ('dont_want', 'Personally chose not to continue with integrated care'), ('advised_to_vertical', 'Healthcare staff asked patient to return to vertical care'), ('referred_out', 'Referred to another facility without an ICC'), ('receives_community_care', 'Patient is currently receiving their HIV care in the community'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If not receiving integrated care, why not?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='eligibility_datetime',
            field=models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to report_datetime', null=True),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='icc_not_in_reason',
            field=models.CharField(choices=[('icc_not_available', 'ICC not available (or closed) in this facility'), ('moved', 'Moved out of area'), ('dont_want', 'Personally chose not to continue with integrated care'), ('advised_to_vertical', 'Healthcare staff asked patient to return to vertical care'), ('referred_out', 'Referred to another facility without an ICC'), ('receives_community_care', 'Patient is currently receiving their HIV care in the community'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If not receiving integrated care, why not?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='screening_consent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Has the subject given his/her verbal consent to be screened for the MOCCA Extension study?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='willing_to_consent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='If No, complete refusal form.', max_length=25, verbose_name='Has the patient expressed willingness to participate in the `MOCCA extension` study'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='eligibility_datetime',
            field=models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to report_datetime', null=True),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='icc_not_in_reason',
            field=models.CharField(choices=[('icc_not_available', 'ICC not available (or closed) in this facility'), ('moved', 'Moved out of area'), ('dont_want', 'Personally chose not to continue with integrated care'), ('advised_to_vertical', 'Healthcare staff asked patient to return to vertical care'), ('referred_out', 'Referred to another facility without an ICC'), ('receives_community_care', 'Patient is currently receiving their HIV care in the community'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If not receiving integrated care, why not?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='screening_consent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Has the subject given his/her verbal consent to be screened for the MOCCA Extension study?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='willing_to_consent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='If No, complete refusal form.', max_length=25, verbose_name='Has the patient expressed willingness to participate in the `MOCCA extension` study'),
        ),
    ]
