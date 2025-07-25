# Generated by Django 5.1.1 on 2025-04-11 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_blog_postdate_alter_event_postdate_career_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedCandidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('CV', models.FileField(upload_to='media/CandidatesCV/')),
                ('Cover_Letter', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 11, 19, 26, 19, 818904)),
        ),
        migrations.AlterField(
            model_name='career',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 11, 19, 26, 19, 818904)),
        ),
        migrations.AlterField(
            model_name='event',
            name='PostDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 11, 19, 26, 19, 817901)),
        ),
    ]
