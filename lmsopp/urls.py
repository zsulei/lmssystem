from django.urls import path
from .views import courses, course_detail


urlpatterns = [
    path('', courses, name='home'),
    path('detail/<int:course_id>/', course_detail, name='course')
]
