# Generated by Django 2.2.4 on 2019-10-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_system', '0013_auto_20191019_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoringcriteria',
            name='t_option1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='scoringcriteria',
            name='t_option2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='scoringcriteria',
            name='t_option3',
            field=models.TextField(blank=True),
        ),
    ]
