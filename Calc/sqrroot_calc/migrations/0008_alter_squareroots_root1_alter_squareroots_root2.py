# Generated by Django 4.0.5 on 2022-06-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqrroot_calc', '0007_alter_squareroots_root1_alter_squareroots_root2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squareroots',
            name='root1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squareroots',
            name='root2',
            field=models.FloatField(),
        ),
    ]
