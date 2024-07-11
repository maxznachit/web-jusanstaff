from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('courses', courses_list, name='list'),
    path('courses/<int:pk>/start', course_start, name='start'),
    path('courses/<int:pk>/schedule', course_graphic_items_list, name='graphic-items-list'),
    path('courses/<int:pk>/schedule/<int:graphic_item_pk>/done', course_graphic_items_done, name='graphic-items-done'),
]
