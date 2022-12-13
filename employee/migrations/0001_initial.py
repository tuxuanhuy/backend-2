# Generated by Django 4.1.4 on 2022-12-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='uploads/')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(default=1, max_length=100)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
            ],
            options={
                'db_table': 'shift',
            },
        ),
    ]
