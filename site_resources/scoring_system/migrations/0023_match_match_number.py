# Generated by Django 2.2.3 on 2020-01-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_system', '0022_auto_20200124_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_number',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]