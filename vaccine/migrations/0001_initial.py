# Generated by Django 3.1.3 on 2021-08-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('vacday', models.DateField(null=True, verbose_name='mm/dd/yyyy')),
                ('prooffile', models.FileField(default='images/none.pdf', upload_to='images')),
            ],
        ),
    ]
