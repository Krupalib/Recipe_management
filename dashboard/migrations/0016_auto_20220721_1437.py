# Generated by Django 3.2.5 on 2022-07-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20220721_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='process_steps',
            name='time_unit',
            field=models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='time_unit',
            field=models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrecipes',
            name='time_unit',
            field=models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours')], max_length=200, null=True),
        ),
    ]
