# Generated by Django 3.2.10 on 2021-12-15 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dukkaapp', '0002_reciepts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reciepts',
            old_name='file_name',
            new_name='file_id',
        ),
    ]
