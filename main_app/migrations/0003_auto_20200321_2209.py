# Generated by Django 3.0.4 on 2020-03-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200321_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='owner',
        ),
        migrations.AddField(
            model_name='package',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='users',
            field=models.ManyToManyField(to='main_app.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]