# Generated by Django 2.0 on 2019-01-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20190117_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.FloatField(default=75),
        ),
        migrations.AlterField(
            model_name='student',
            name='serial_no',
            field=models.IntegerField(default=1, max_length=100, primary_key=True, serialize=False),
        ),
    ]
