# Generated by Django 3.1.3 on 2021-08-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_orderer_paymode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='merit',
            field=models.IntegerField(default=100),
        ),
    ]
