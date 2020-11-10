# Generated by Django 3.1.3 on 2020-11-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('know_your_priest', '0003_auto_20201109_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priest',
            old_name='date',
            new_name='date_of_birth',
        ),
        migrations.AddField(
            model_name='priest',
            name='profile_pic',
            field=models.ImageField(default=None, upload_to='profiles'),
        ),
    ]
