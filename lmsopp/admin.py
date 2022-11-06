from django.contrib import admin
from .models import Student, Course, Task, Payment, Teacher
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Payment)
admin.site.register(Teacher)
