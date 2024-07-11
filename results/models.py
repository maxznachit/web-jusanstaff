from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, GraphicItem

# Create your models here.

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progresses') # ForeignKey = one-to-many, бізге one-to-one қажет
    graphic_item = models.ForeignKey(GraphicItem, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    completed = models.BooleanField('Орындалды',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.pk} | {self.user} | {self.graphic_item}'