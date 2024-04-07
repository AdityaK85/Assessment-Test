# Generated by Django 5.0.4 on 2024-04-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('password', models.CharField(blank=True, max_length=300, null=True)),
                ('my_referral_code', models.CharField(blank=True, max_length=300, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
