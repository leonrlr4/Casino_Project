# Generated by Django 2.0.4 on 2018-05-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_auto_20180427_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('date', models.DateTimeField(db_column='date', max_length=100, primary_key=True, serialize=False)),
                ('period', models.CharField(db_column='period', max_length=2)),
            ],
        ),
    ]