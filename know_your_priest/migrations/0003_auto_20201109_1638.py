# Generated by Django 3.1.2 on 2020-11-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('know_your_priest', '0002_auto_20201109_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priest',
            name='about',
            field=models.CharField(max_length=1000),
        ),
    ]
