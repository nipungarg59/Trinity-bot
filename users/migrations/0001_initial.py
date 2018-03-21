# Generated by Django 2.0.1 on 2018-03-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(default='Codeforces', max_length=255)),
                ('platform_id', models.BigIntegerField()),
                ('contest_name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('phase', models.CharField(max_length=255)),
                ('frozen', models.BooleanField()),
                ('duration_seconds', models.BigIntegerField()),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]