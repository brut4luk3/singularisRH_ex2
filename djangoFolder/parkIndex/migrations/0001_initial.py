# Generated by Django 5.0.2 on 2024-02-08 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_description', models.CharField(max_length=50)),
                ('contract_max_value', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_contract',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=50)),
                ('cus_card_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_customer',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_description', models.CharField(max_length=50)),
                ('plan_value', models.FloatField()),
            ],
            options={
                'db_table': 'tb_plan',
            },
        ),
        migrations.CreateModel(
            name='ContractRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('until', models.IntegerField()),
                ('value', models.FloatField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkIndex.contract')),
            ],
            options={
                'db_table': 'tb_contract_rule',
            },
        ),
        migrations.CreateModel(
            name='CustomerPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkIndex.customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkIndex.plan')),
            ],
            options={
                'db_table': 'tb_customer_plan',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_plate', models.CharField(max_length=10)),
                ('vehicle_model', models.CharField(blank=True, max_length=30, null=True)),
                ('vehicle_description', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parkIndex.customer')),
            ],
            options={
                'db_table': 'tb_vehicle',
            },
        ),
        migrations.CreateModel(
            name='ParkMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField()),
                ('exit_date', models.DateTimeField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkIndex.vehicle')),
            ],
            options={
                'db_table': 'tb_park_movement',
            },
        ),
    ]
