# Generated by Django 2.2.2 on 2019-07-14 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0017_auto_20190714_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donors',
            name='password',
        ),
    ]