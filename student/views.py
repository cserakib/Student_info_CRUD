from django.shortcuts import render, redirect
from .models import Student
# from .forms import StudentForm
# Create your views here.
def index(request):
    student = Student.objects.all()
    context ={'student': student}
    return render(request, 'index.html', context)

def Create(request):
    print(request.POST)
    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']
    city = request.GET['city']

    Student_name_details = Student(name=name, phone=phone, email=email,city=city)
    Student_name_details.save()
    return redirect('index')

def add_studnet(request):
    return render(request,'add_students.html')

def delete(request, id):
    studnet = Student.objects.get(pk=id)
    studnet.delete()
    return redirect('index')

def edit(request, id):

    student = Student.objects.get(pk=id)
    context ={'student': student}
    return render(request, 'edit.html', context)

def update(request, id):
    student = Student.objects.get(pk=id)
    student.name = request.GET['name']
    student.phone = request.GET['phone']
    student.email = request.GET['email']
    student.city = request.GET['city']

    student.save()
    return redirect('index')