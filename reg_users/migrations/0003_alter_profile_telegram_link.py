# Generated by Django 4.1.6 on 2023-02-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_users', '0002_rename_profile_report_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_link',
            field=models.CharField(max_length=50, unique=True, verbose_name='профиль в телеграм'),
        ),
    ]
