# Generated by Django 4.0.6 on 2022-09-27 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_form_options_alter_form_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='desription',
            field=models.TextField(blank=True, null=True),
        ),
    ]