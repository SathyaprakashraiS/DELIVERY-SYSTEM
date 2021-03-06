# Generated by Django 3.1.3 on 2021-08-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_vform_dosecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vform',
            name='dosecount',
            field=models.IntegerField(default=0, verbose_name='DOSES VACCINATED'),
        ),
        migrations.AlterField(
            model_name='vform',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='NAME'),
        ),
        migrations.AlterField(
            model_name='vform',
            name='prooffile',
            field=models.FileField(default='images/none.pdf', upload_to='images', verbose_name='PROOF FILE'),
        ),
        migrations.AlterField(
            model_name='vform',
            name='vacday',
            field=models.DateField(null=True, verbose_name='LAST VACCINATED DATE: MM/DD/YYYY'),
        ),
    ]
