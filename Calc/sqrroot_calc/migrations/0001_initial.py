# Generated by Django 4.0.5 on 2022-06-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('c', models.IntegerField()),
                ('root1', models.CharField(max_length=20)),
                ('root2', models.CharField(max_length=20)),
            ],
        ),
    ]
