# Generated by Django 3.0.5 on 2020-08-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
