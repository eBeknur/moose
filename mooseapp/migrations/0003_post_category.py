# Generated by Django 5.1.3 on 2024-11-14 09:17

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mooseapp", "0002_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="mooseapp.category",
            ),
            preserve_default=False,
        ),
    ]
