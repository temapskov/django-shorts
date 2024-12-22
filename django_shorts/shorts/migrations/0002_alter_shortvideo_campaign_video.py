# Generated by Django 5.1.4 on 2024-12-22 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shorts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shortvideo",
            name="campaign",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="short_videos",
                to="shorts.campaign",
            ),
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_file", models.FileField(upload_to="videos/")),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="shorts.campaign",
                    ),
                ),
            ],
        ),
    ]