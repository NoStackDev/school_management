# Generated by Django 4.1 on 2022-08-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
