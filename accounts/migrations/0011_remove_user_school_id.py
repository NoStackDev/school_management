# Generated by Django 4.1 on 2022-08-10 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_user_school_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school_id',
        ),
    ]