# Generated by Django 3.1.3 on 2021-08-12 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20210812_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['areaname']},
        ),
        migrations.RenameField(
            model_name='area',
            old_name='name',
            new_name='areaname',
        ),
    ]
