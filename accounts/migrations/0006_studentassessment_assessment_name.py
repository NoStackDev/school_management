# Generated by Django 4.1 on 2022-09-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_studentassessment_delete_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassessment',
            name='assessment_name',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]