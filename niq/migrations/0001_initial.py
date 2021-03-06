# Generated by Django 3.2.12 on 2022-03-28 10:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(default='Intern', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='niq.employee')),
                ('m_name', models.CharField(max_length=200)),
            ],
            bases=('niq.employee',),
        ),
        migrations.AddField(
            model_name='employee',
            name='reports_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='niq.manager'),
        ),
    ]
