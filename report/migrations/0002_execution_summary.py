# Generated by Django 2.1.5 on 2019-04-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='execution_summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcname', models.CharField(max_length=150)),
                ('suite', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('reference_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.execution_details')),
            ],
        ),
    ]
