# Generated by Django 5.1.4 on 2025-01-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_internprofile_first_name_internprofile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
