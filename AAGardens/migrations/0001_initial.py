# Generated by Django 4.0.2 on 2022-08-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMS_OTP',
            fields=[
                ('OTP_Id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=250)),
                ('MobileNumber', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('OTP', models.IntegerField()),
            ],
        ),
    ]