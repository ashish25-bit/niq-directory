# Generated by Django 3.2.12 on 2022-03-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='reports_to',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
