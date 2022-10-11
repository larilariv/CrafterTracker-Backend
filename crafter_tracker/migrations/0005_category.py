# Generated by Django 4.0.6 on 2022-10-11 01:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crafter_tracker', '0004_project_complete_date_project_create_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]