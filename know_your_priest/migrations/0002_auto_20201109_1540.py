# Generated by Django 3.1.2 on 2020-11-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('know_your_priest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priest',
            name='about',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='priest',
            name='associations',
            field=models.CharField(max_length=500),
        ),
    ]
