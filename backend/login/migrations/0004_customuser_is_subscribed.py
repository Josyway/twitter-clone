# Generated by Django 5.1.2 on 2024-11-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_customuser_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_subscribed",
            field=models.BooleanField(default=False),
        ),
    ]
