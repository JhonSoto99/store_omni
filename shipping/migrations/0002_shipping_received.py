# Generated by Django 3.2.6 on 2021-08-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]