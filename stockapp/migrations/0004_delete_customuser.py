# Generated by Django 4.2.5 on 2023-09-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
