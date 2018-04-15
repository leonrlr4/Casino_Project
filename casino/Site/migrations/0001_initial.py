# Generated by Django 2.0.4 on 2018-04-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login1',
            fields=[
                ('name', models.CharField(db_column='name', max_length=20)),
                ('account', models.CharField(db_column='account', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(db_column='password', max_length=20)),
                ('sn1', models.CharField(blank=True, db_column='sn1', max_length=20)),
                ('sn2', models.CharField(blank=True, db_column='sn2', max_length=20)),
                ('sn3', models.CharField(blank=True, db_column='sn3', max_length=20)),
                ('certified', models.IntegerField(db_column='certified', max_length=3)),
                ('money', models.IntegerField(db_column='money', max_length=10)),
                ('bet', models.IntegerField(db_column='bet', max_length=10)),
                ('totalMoney', models.IntegerField(db_column='totalMoney', max_length=10)),
                ('totalIntro', models.IntegerField(db_column='totalIntro', max_length=10)),
                ('totalPer', models.IntegerField(db_column='totalPer', max_length=3)),
                ('introBet', models.IntegerField(db_column='introBet', max_length=10)),
                ('authority', models.IntegerField(db_column='authority', max_length=3)),
            ],
        ),
    ]