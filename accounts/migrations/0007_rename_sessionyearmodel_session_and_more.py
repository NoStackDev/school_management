# Generated by Django 4.1 on 2022-08-09 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_school_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SessionYearModel',
            new_name='Session',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='session_year_id',
            new_name='session',
        ),
    ]