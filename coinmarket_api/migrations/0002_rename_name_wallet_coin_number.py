# Generated by Django 4.0.4 on 2022-05-31 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarket_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='name',
            new_name='coin_number',
        ),
    ]