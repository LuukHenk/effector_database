# Generated by Django 3.1.6 on 2021-02-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20210222_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='effector_signal_peptide',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False'), ('', '')], default='A', max_length=1),
        ),
    ]