from api.views import *
from django.urls import path


urlpatterns = [
    path('greeting/', greeting),
    path('student/', students),
    path('student/detail/', students_json),
    path('faculty/', table),
    path('subject/', subjects_json),
    path('courses/', show_courses),
]