from django.contrib import admin
from api.models import Student, Faculty, Institute, Department, SubjectType, Subject, Course, CourseType, FacultyType

# Register your models here.
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(SubjectType)
admin.site.register(Subject)
admin.site.register(FacultyType)