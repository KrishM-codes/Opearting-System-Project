# Generated by Django 5.0.2 on 2024-03-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simulator', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='Completion_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Completion Time'),
        ),
        migrations.AlterField(
            model_name='process',
            name='Arrival_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='process',
            name='Burst_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Burst Time'),
        ),
        migrations.AlterField(
            model_name='process',
            name='Process_name',
            field=models.CharField(max_length=10, null=True, verbose_name='Process Name'),
        ),
        migrations.AlterField(
            model_name='process',
            name='Turnaround_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Turnaround Time'),
        ),
        migrations.AlterField(
            model_name='process',
            name='Waiting_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Waiting Time'),
        ),
    ]