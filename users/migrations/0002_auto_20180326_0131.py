# Generated by Django 2.0.1 on 2018-03-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='contests',
            index_together={('platform', 'platform_id')},
        ),
    ]