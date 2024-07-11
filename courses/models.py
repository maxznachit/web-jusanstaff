from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.


def upload_to(instance, filename: str, *args, **kwargs):
    current_datetime = datetime.now()
    current_datetime_str = '{:%Y/%m/%d/%H/%M/%S}-{}'.format(
        current_datetime, filename)
    return current_datetime_str


class Course(models.Model):
    title = models.CharField('Title', max_length=100)
    intensity = models.CharField('Continuity', max_length=50)
    tumbnail_image = models.ImageField(
        upload_to=upload_to, null=False)
    description = models.TextField('Description',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.pk} | {self.title}'


class GraphicItem(models.Model):
    title = models.CharField('Title', max_length=100)
    course = models.ForeignKey(
        Course, null=False, on_delete=models.CASCADE, related_name='graphic_items')
    day_order = models.PositiveIntegerField('Numeration')
    description = RichTextUploadingField('Description', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.pk} | {self.course} | {self.title}'
