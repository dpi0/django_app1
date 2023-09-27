# Generated by Django 4.2.5 on 2023-09-27 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_topic_post_owner_post_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["updated_at", "created_at"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
