# Generated by Django 3.2.6 on 2021-08-16 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='created date', null=True, verbose_name='created date')),
                ('changed_at', models.DateTimeField(auto_now=True, help_text='updated date', null=True, verbose_name='updated date')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(help_text='Descriptive name.', max_length=50)),
                ('description', models.TextField(max_length=600)),
                ('price', models.PositiveIntegerField(default=0)),
                ('enabled', models.BooleanField(default=False, help_text='Helps to easily distinguish the condition of the product.')),
                ('changed_by', models.ForeignKey(blank=True, editable=False, help_text='Who changed it?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_changed_by', to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
                ('created_by', models.ForeignKey(blank=True, editable=False, help_text='Who created it?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]