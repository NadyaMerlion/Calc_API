# Generated by Django 4.0.5 on 2022-06-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqrroot_calc', '0003_alter_number_root1_alter_number_root2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='root1',
        ),
        migrations.RemoveField(
            model_name='number',
            name='root2',
        ),
    ]
