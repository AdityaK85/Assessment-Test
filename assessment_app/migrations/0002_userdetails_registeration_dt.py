# Generated by Django 5.0.4 on 2024-04-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='registeration_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
