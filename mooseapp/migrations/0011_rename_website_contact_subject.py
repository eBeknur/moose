# Generated by Django 5.1.3 on 2024-11-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mooseapp", "0010_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="website",
            new_name="subject",
        ),
    ]
