# Generated by Django 4.0.6 on 2022-10-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafter_tracker', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, to='crafter_tracker.category'),
        ),
    ]
