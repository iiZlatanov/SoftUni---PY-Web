# Generated by Django 4.2.16 on 2024-11-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
