# Generated by Django 5.1.2 on 2024-10-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_students_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='studentid',
            field=models.IntegerField(unique=True),
        ),
    ]
