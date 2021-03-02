# Generated by Django 3.1.6 on 2021-03-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocca_subject', '0017_auto_20210302_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cholmedicationadherence',
            name='pill_count',
            field=models.IntegerField(null=True, verbose_name='Number of pills left in the bottle'),
        ),
        migrations.AlterField(
            model_name='dmmedicationadherence',
            name='pill_count',
            field=models.IntegerField(null=True, verbose_name='Number of pills left in the bottle'),
        ),
        migrations.AlterField(
            model_name='historicalcholmedicationadherence',
            name='pill_count',
            field=models.IntegerField(null=True, verbose_name='Number of pills left in the bottle'),
        ),
        migrations.AlterField(
            model_name='historicaldmmedicationadherence',
            name='pill_count',
            field=models.IntegerField(null=True, verbose_name='Number of pills left in the bottle'),
        ),
        migrations.AlterField(
            model_name='historicalhivmedicationadherence',
            name='last_missed_pill',
            field=models.CharField(choices=[('today', 'today'), ('yesterday', 'yesterday'), ('earlier_this_week', 'earlier this week'), ('last_week', 'last week'), ('lt_month_ago', 'less than a month ago'), ('gt_month_ago', 'more than a month ago'), ('NEVER', 'have never missed taking my pills')], max_length=25, verbose_name='When was the last time you missed taking your <U>condition_label</U> medication?'),
        ),
        migrations.AlterField(
            model_name='historicalhtnmedicationadherence',
            name='last_missed_pill',
            field=models.CharField(choices=[('today', 'today'), ('yesterday', 'yesterday'), ('earlier_this_week', 'earlier this week'), ('last_week', 'last week'), ('lt_month_ago', 'less than a month ago'), ('gt_month_ago', 'more than a month ago'), ('NEVER', 'have never missed taking my pills')], max_length=25, verbose_name='When was the last time you missed taking your <U>condition_label</U> medication?'),
        ),
        migrations.AlterField(
            model_name='hivmedicationadherence',
            name='last_missed_pill',
            field=models.CharField(choices=[('today', 'today'), ('yesterday', 'yesterday'), ('earlier_this_week', 'earlier this week'), ('last_week', 'last week'), ('lt_month_ago', 'less than a month ago'), ('gt_month_ago', 'more than a month ago'), ('NEVER', 'have never missed taking my pills')], max_length=25, verbose_name='When was the last time you missed taking your <U>condition_label</U> medication?'),
        ),
        migrations.AlterField(
            model_name='htnmedicationadherence',
            name='last_missed_pill',
            field=models.CharField(choices=[('today', 'today'), ('yesterday', 'yesterday'), ('earlier_this_week', 'earlier this week'), ('last_week', 'last week'), ('lt_month_ago', 'less than a month ago'), ('gt_month_ago', 'more than a month ago'), ('NEVER', 'have never missed taking my pills')], max_length=25, verbose_name='When was the last time you missed taking your <U>condition_label</U> medication?'),
        ),
    ]
