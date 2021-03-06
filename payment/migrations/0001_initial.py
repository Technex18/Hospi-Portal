# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-11 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reg', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='currentHostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DeskTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorityLevel', models.SmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('maxPrice', models.IntegerField()),
                ('offeredPrice', models.IntegerField()),
                ('facilityType', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('capacity', models.IntegerField(default=0)),
                ('genderType', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attemptNumber', models.SmallIntegerField(default=1)),
                ('idCardNumber', models.IntegerField(default=0)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Facility')),
                ('techProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.TechProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OffLineProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.SmallIntegerField(default=1)),
                ('hostel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.Hostel')),
                ('techProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.TechProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('crediter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.TechProfile')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Facility')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.DeskTeam')),
            ],
        ),
        migrations.AddField(
            model_name='currenthostel',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Hostel'),
        ),
    ]
