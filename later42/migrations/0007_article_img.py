# Generated by Django 4.1.3 on 2022-11-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("later42", "0006_remove_url_content_remove_url_title_article_short_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="img",
            field=models.URLField(blank=True, null=True),
        ),
    ]
