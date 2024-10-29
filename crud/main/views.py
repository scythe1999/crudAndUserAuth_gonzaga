from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Students
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('homepage')  
        else:
            return render(request, 'assets/login.html', {'error': 'Invalid credentials'})
    return render(request, 'assets/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    students = Students.objects.all()
    student_data = serializers.serialize('json', students)
    context = {'students': students, 'student_data': student_data}
    return render(request, 'assets/lists.html', context)

def create(request):
    if request.method == 'POST':
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        studentid = request.POST.get('studentid')
        section = request.POST.get('section')

        try:
            Students.objects.create(
                lastname=lastname,
                firstname=firstname,
                studentid=studentid,
                section=section
            )
            messages.success(request, 'Student Added!')
        except IntegrityError:
            messages.error(request, 'Student ID already exists. Please use a different ID.')

    return redirect(reverse('homepage'))

def delete(request, pk):
    studenttodelete = get_object_or_404(Students, id=pk) 
    studenttodelete.delete()  
    return redirect(reverse('homepage'))

def update(request, pk):
    student = get_object_or_404(Students, id=pk)

    if request.method == 'POST':
        student.firstname = request.POST.get('firstname_update')
        student.lastname = request.POST.get('lastname_update')
        student.studentid = request.POST.get('studentid_update')
        student.section = request.POST.get('section_update')
        
        try:
            student.save()
            messages.success(request, 'Student updated successfully!')
        except IntegrityError:
            messages.error(request, 'Failed to update: Student ID already exists.')
        
    return redirect(reverse('homepage'))