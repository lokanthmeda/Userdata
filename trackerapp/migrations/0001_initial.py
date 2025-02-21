# Generated by Django 3.1.6 on 2021-02-10 06:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9A-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=200)),
                ('time_zone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.TimeField(null=True)),
                ('s_time', models.DateTimeField()),
                ('e_time', models.DateTimeField()),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackerapp.user')),
            ],
        ),
    ]
