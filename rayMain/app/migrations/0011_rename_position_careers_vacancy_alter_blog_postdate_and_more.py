# Generated by Django 5.1.1 on 2025-04-10 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_careerscategory_alter_blog_postdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careers',
            old_name='position',
            new_name='vacancy',
        ),
        migrations.AlterField(
            model_name='blog',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 10, 19, 9, 51, 740813)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 10, 19, 9, 51, 741814)),
        ),
        migrations.AlterField(
            model_name='event',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 10, 19, 9, 51, 740813)),
        ),
    ]
