# Generated by Django 2.0 on 2019-01-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('class_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('number_of_students', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('class_studying', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('age', models.IntegerField(null=True)),
                ('qualification', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('classes_taught', models.ManyToManyField(to='myapp.ClassRoom')),
            ],
        ),
    ]