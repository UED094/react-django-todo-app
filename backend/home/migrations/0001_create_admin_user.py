# Generated by Django 4.2.6 on 2023-12-12 02:37

from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='admin',
        password='admin',
        email='admin@example.com'
    )

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
