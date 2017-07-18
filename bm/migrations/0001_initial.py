# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('account_holder', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.BigIntegerField(default=None)),
                ('account_type', models.CharField(max_length=30)),
                ('pancard_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('branch_name', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=None)),
                ('time', models.TimeField(default=None)),
                ('amount', models.IntegerField(default=None)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bm.Account')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bm.Bank')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bm.Bank'),
        ),
    ]