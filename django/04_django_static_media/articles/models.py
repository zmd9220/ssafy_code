from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='jpeg',
        options={'quality': 90},
        upload_to='%Y/%m/%d/',
        # upload_to=articles_image_path,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
