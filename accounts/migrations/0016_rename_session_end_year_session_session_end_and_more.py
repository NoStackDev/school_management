# Generated by Django 4.1 on 2022-08-15 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_rename_staff_id_subject_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='session_end_year',
            new_name='session_end',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='session_start_year',
            new_name='session_start',
        ),
    ]