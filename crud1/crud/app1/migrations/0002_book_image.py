# Generated by Django 5.0.4 on 2024-05-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="books"),
        ),
    ]
