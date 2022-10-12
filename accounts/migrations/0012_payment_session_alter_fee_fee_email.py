# Generated by Django 4.1 on 2022-10-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_studentassessment_assessment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='session',
            field=models.CharField(default='2021/2022', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fee',
            name='fee_email',
            field=models.EmailField(default='isaiah.idonije55@gmail.com', max_length=255),
        ),
    ]
