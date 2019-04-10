# Generated by Django 2.1 on 2018-08-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180810_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcelink',
            name='owner',
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='content_objectives',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='language_objectives',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.RemoveField(
            model_name='lessonplan',
            name='resource_links',
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='resource_links',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='ResourceLink',
        ),
    ]
