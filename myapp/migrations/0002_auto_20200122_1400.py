# Generated by Django 2.2 on 2020-01-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='price',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='time',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]