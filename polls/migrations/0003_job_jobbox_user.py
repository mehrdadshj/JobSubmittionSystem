# Generated by Django 2.2.5 on 2019-09-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0002_auto_20190928_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('BoxId', models.TextField()),
                ('InitialTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JobBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('InitialTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField()),
                ('LastName', models.TextField()),
                ('Email', models.TextField()),
                ('Password', models.CharField(max_length=200)),
                ('Picture', models.TextField()),
                ('PhoneNumber', models.TextField()),
            ],
        ),
    ]