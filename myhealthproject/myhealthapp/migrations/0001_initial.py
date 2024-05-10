# Generated by Django 5.0.6 on 2024-05-10 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('academic_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('attendance_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('enrollment_year', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhealthapp.class')),
            ],
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('health_status', models.CharField(choices=[('', '空欄'), ('sick', '病欠'), ('absent', '事故欠')], default='', max_length=100)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhealthapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhealthapp.class')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhealthapp.user')),
            ],
        ),
    ]
