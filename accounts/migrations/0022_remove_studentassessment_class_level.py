# Generated by Django 4.1 on 2022-11-17 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_studentassessment_class_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentassessment',
            name='class_level',
        ),
    ]
