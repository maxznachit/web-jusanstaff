from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Course, GraphicItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from results.models import UserProgress
import json

# Create your views here.


def courses_list(request):
    courses = Course.objects.all().annotate(
        graphic_items_count=Count('graphic_items'))
    user = request.user
    user_progress_courses_ids = []
    if user and user.is_authenticated:
        user_progress_courses_ids = user.progresses.all().values_list('course_id', flat=True)
        user_progress_courses_ids = set(user_progress_courses_ids)
    return render(request, 'courses/course_list.html', context={
        'courses': courses,
        'user_progress_courses_ids': user_progress_courses_ids,
    })


@login_required
def course_start(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user
    progresses = user.progresses.filter(course=course)
    if progresses.exists():
        return redirect('courses:graphic-items-list', pk=course.pk)
    first_item = course.graphic_items.filter(day_order=1)
    if not first_item.exists():
        return HttpResponseServerError("No schedule in this task")
    first_item = first_item.last()
    UserProgress.objects.create(
        user=user,
        graphic_item=first_item,
        course=course,
        completed=False,
    )
    return redirect('courses:graphic-items-list', pk=course.pk)


def course_graphic_items_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course_graphic_items = course.graphic_items.all()
    user = request.user
    progresses_ids = user.progresses.filter(
        course=course).values_list('graphic_item_id', flat=True)
    return render(request, 'courses/course_graphic_items_list.html', context={
        'graphic_items_dict': [
            {
                'id': i.id,
                'title': i.title,
                'description': i.description,
                'completed': 1 if i.pk in progresses_ids else 0,
                'course_id': course.pk,
            } for i in course_graphic_items
        ],
        'course': course,
    })


@login_required
def course_graphic_items_done(request, pk, graphic_item_pk):
    course = get_object_or_404(Course, pk=pk)
    course_graphic_item = get_object_or_404(GraphicItem, pk=graphic_item_pk)
    progress, created = UserProgress.objects.get_or_create(
        course=course,
        graphic_item=course_graphic_item,
        user=request.user,
    )
    progress.completed = True
    progress.save()
    return redirect('courses:graphic-items-list', pk=course.pk)
