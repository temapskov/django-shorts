from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Campaign, ShortVideo
from .schemas import CampaignSchema, ShortVideoSchema, VideoSchema

router = Router()


@router.get("/campaigns/", response=List[CampaignSchema])
def list_campaigns(request):
    """Возвращает список всех рекламных кампаний."""
    campaigns = Campaign.objects.all()
    return [
        CampaignSchema(
            id=c.id, name=c.name, description=c.description, created_at=c.created_at
        )
        for c in campaigns
    ]


@router.get("/videos/", response=List[ShortVideoSchema])
def list_videos(request, campaign_id: int):
    """Возвращает список видео из выбранной кампании."""
    campaign = get_object_or_404(Campaign, id=campaign_id)
    videos = ShortVideo.objects.filter(campaign=campaign).order_by("-created_at")
    return [
        ShortVideoSchema(
            id=v.id,
            title=v.title,
            video=v.video.url,  # Обязательно используйте `.url` для доступа к пути файла
            campaign=v.campaign.name,
            created_at=v.created_at,
            likes=v.likes,
            views=v.views,
        )
        for v in videos
    ]


@router.get("/campaigns/{campaign_id}/videos", response=list[VideoSchema])
def get_campaign_videos(request, campaign_id: int):
    campaign = Campaign.objects.get(id=campaign_id)
    videos = campaign.videos.all()

    # Сериализуем видео объекты в формат, который ожидает схема
    video_data = []
    for video in videos:
        # Преобразуем поля в URL строки
        video_data.append(
            VideoSchema(
                id=video.id,
                title=video.title,
                description=video.description,
                video_file=(
                    video.video_file.url if video.video_file else ""
                ),  # Получаем URL для видео
                thumbnail=(
                    video.thumbnail.url if video.thumbnail else None
                ),  # Получаем URL для миниатюры
                uploaded_at=video.uploaded_at,
            )
        )

    return video_data
