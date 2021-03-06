# Generated by Django 2.2.3 on 2020-01-23 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_system', '0019_delete_eventuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.SmallIntegerField()),
                ('red_team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scoring_system.Team')),
            ],
        ),
    ]
