# Generated by Django 2.2 on 2019-06-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20190604_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='serial_no',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
