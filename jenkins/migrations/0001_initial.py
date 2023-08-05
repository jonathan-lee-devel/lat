# Generated by Django 4.2.4 on 2023-08-04 23:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('date_added', models.DateTimeField(auto_created=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('date_added', models.DateTimeField(auto_created=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('number', models.IntegerField(default=0)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jenkins.job')),
            ],
        ),
    ]
