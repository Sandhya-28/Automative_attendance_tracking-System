# Generated by Django 5.0.6 on 2024-06-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_employee_face_encoding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='face_encoding',
        ),
    ]
