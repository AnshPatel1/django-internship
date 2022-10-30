from django.shortcuts import render
from django.http import HttpResponse
from api.models import *
import json
# Create your views here.

def home(request):
    return HttpResponse("foabeg;ouiefaoihfois")

def greeting(request):
    return HttpResponse("Hello Nonsense World")

def subjects_json(request):
    subjects = Subject.objects.all()
    ret_list = []
    for subject in subjects:
        tmp = {}
        tmp['code'] = subject.code
        tmp["name"] = subject.name
        tmp['abbreviation'] = subject.abbreviation
        tmp['type'] = subject.type.id
        tmp['course'] = subject.course.course_id
        ret_list.append(tmp)
        
    return HttpResponse(json.dumps(ret_list), content_type="application/json")
    

def students(request):
    students = Student.objects.all()
    ret_value = ""
    for student in students:
        ret_value += student.name + "<br>"
        
    return HttpResponse(ret_value)

def students_json(request):
    students = Student.objects.all()
    ret_list = []
    for student in students:
        ret_value = {}
        ret_value['name'] = student.name
        ret_value['enrollment'] = student.enrollment
        ret_value['address'] = student.address
        ret_value['email'] = student.email
        ret_value['mobile'] = student.mobile
        ret_list.append(ret_value)
        
    return HttpResponse(json.dumps(ret_list), content_type="application/json")


def table(request):
    students = Student.objects.all()
    context = {}
    ret_list = []
    for student in students:
        ret_list.append(student)
    context['students'] = ret_list
    return render(request, 'tables.html', context)


def show_courses(request):
    courses = Course.objects.all()
    courses = list(courses)
    context = {"courses" : courses}
    return render(request, 'courses.html', context)