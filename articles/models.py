from django.db import models
from datetime import datetime, timedelta, timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


def upload_to(instance, filename: str, *args, **kwargs):
    current_datetime = datetime.now()
    current_datetime_str = '{:%Y/%m/%d/%H/%M/%S}-{}'.format(
        current_datetime, filename)
    return current_datetime_str


class Article(models.Model):
    title = models.CharField("Атауы", max_length=100)
    tumbnail_image = models.ImageField(
        upload_to=upload_to, null=False)
    content = RichTextUploadingField('Контент', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.pk} | {self.title}'

    @property
    def truncated_content(self):
        max_length = 100
        if len(self.content) > max_length:
            return f"{self.content[:max_length]}..."
        else:
            return self.content
