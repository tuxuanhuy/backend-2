# Generated by Django 4.1.4 on 2022-12-13 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
