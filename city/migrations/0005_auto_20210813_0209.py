# Generated by Django 3.1.3 on 2021-08-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_area_maplink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='maplink',
            field=models.CharField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.001696423075!2d79.15722781561198!3d12.971742990855768!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bad479f0ccbe067%3A0xfef222e5f36ecdeb!2sVellore%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1628800616114!5m2!1sen!2sin', max_length=1000),
        ),
    ]