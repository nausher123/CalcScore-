# Generated by Django 4.0.6 on 2022-09-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markcheck', '0003_thresholddata_o'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sat_Curves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=7)),
                ('curve_type', models.CharField(max_length=15)),
                ('raw_score_math', models.IntegerField()),
                ('raw_score_read', models.IntegerField()),
                ('raw_score_write', models.IntegerField()),
                ('points_math', models.IntegerField()),
                ('points_read', models.IntegerField()),
                ('points_write', models.IntegerField()),
            ],
        ),
    ]
