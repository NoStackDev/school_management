# Generated by Django 4.1 on 2022-11-09 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_term_current_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='term_enrolled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.term'),
        ),
    ]
