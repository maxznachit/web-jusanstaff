from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course

# Create your views here.


@login_required
def progress_list(request):
    user = request.user
    courses = Course.objects.all()
    data = []
    for course in courses:
        user_progresses = user.progresses.filter(course=course)
        if user_progresses:
            data.append({
                'course': course,
                'progresses': user_progresses,
            })
    return render(request, 'results/progress_list.html', {
        'data': data
    })
