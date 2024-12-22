from datetime import datetime

from pydantic import BaseModel, ConfigDict


class VideoSchema(BaseModel):
    id: int
    title: str
    description: str
    video_file: str  # URL видео
    thumbnail: str | None  # URL для миниатюры
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CampaignSchema(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime


class ShortVideoSchema(BaseModel):
    id: int
    title: str
    video: str
    campaign: str
    created_at: datetime
    likes: int
    views: int
