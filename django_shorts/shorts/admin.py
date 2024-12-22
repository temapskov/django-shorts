from django.contrib import admin

from .models import Campaign, ShortVideo, Video


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(ShortVideo)
class ShortVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "campaign", "created_at", "likes", "views")


@admin.register(Video)
class ShortVideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "campaign",
        "uploaded_at",
        "thumbnail",
        "video_file",
        "description",
    )
