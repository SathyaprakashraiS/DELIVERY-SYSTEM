# Generated by Django 3.1.3 on 2021-08-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210811_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderer',
            name='reslev',
            field=models.IntegerField(default=1),
        ),
    ]