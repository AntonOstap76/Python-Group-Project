# Generated by Django 5.0.1 on 2024-01-14 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_vy',
            new_name='created_by',
        ),
    ]
