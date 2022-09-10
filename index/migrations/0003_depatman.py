# Generated by Django 4.1 on 2022-08-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_atik_options_atik_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='depatman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(auto_created=True, max_length=100, unique=True)),
                ('non', models.CharField(max_length=45)),
                ('vil_prensipal', models.CharField(max_length=45)),
                ('sipefisi', models.IntegerField()),
                ('slug', models.CharField(max_length=45)),
            ],
        ),
    ]