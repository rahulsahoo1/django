# Generated by Django 2.2 on 2020-03-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200313_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description adsjf gsrkgshksthln  , lkjkjb jhkj nk hug'),
            preserve_default=False,
        ),
    ]