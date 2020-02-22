# Generated by Django 2.2.9 on 2020-02-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inte_subject', '0006_auto_20200220_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='baselinecarestatus',
            name='hiv_willing_to_transfer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=50, verbose_name='Would you be willing to transfer to this facility?'),
        ),
        migrations.AddField(
            model_name='baselinecarestatus',
            name='ncd_willing_to_transfer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=50, verbose_name='Would you be willing to transfer to this facility?'),
        ),
        migrations.AddField(
            model_name='historicalbaselinecarestatus',
            name='hiv_willing_to_transfer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=50, verbose_name='Would you be willing to transfer to this facility?'),
        ),
        migrations.AddField(
            model_name='historicalbaselinecarestatus',
            name='ncd_willing_to_transfer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=50, verbose_name='Would you be willing to transfer to this facility?'),
        ),
    ]
