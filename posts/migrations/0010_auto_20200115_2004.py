# Generated by Django 3.0.2 on 2020-01-15 19:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200114_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field', tinymce.models.HTMLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
