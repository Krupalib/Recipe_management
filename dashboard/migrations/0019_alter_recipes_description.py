# Generated by Django 3.2.5 on 2022-08-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_recipes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
