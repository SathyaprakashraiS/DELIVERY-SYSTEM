# Generated by Django 3.1.3 on 2021-08-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_orderer_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderer',
            name='done',
            field=models.CharField(default=0, max_length=5),
        ),
    ]