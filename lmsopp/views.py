from django.shortcuts import render
from .models import Course, Task, Student, Payment, Teacher


def courses(request):
    return render(request, 'lms/home.html', {
        'courses': Course.objects.all(),
        'teacher': Student.objects.all(),
        'payments': Payment.objects.all(),
    })


def course_detail(request, course_id):
    return render(request, 'lms/course.html', {
        'course': Course.objects.get(id=course_id),
        'tasks': Task.objects.all(),
    })
