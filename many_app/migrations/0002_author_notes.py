# Generated by Django 3.0.5 on 2020-04-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
