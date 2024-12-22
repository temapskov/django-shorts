from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    campaign = models.ForeignKey(
        Campaign, related_name="videos", on_delete=models.CASCADE
    )
    video_file = models.FileField(upload_to="videos/")
    thumbnail = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ShortVideo(models.Model):
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="short_videos"
    )
    title = models.CharField(max_length=255, blank=True)
    video = models.FileField(upload_to="shorts/")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.campaign.name})"
