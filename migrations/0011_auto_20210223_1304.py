# Generated by Django 3.1.6 on 2021-02-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20210223_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='effector_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]