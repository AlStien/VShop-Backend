# Generated by Django 3.2.8 on 2021-11-02 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='email',
            new_name='otpEmail',
        ),
    ]
