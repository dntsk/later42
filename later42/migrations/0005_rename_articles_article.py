"""Generated by Django 4.1.2 on 2022-11-05 17:11"""

from django.db import migrations


class Migration(migrations.Migration):
    """Migration"""

    dependencies = [
        ("later42", "0004_articles"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Articles",
            new_name="Article",
        ),
    ]
