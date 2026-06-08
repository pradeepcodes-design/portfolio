from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Marks

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        Student.objects.create(
            register_number=request.POST['register_number'],
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
        )
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'title': 'Add Student'})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.register_number = request.POST['register_number']
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.department = request.POST['department']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'student': student, 'title': 'Update Student'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

def marks_manage(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks, created = Marks.objects.get_or_create(student=student)
    if request.method == 'POST':
        marks.subject1 = int(request.POST['subject1'])
        marks.subject2 = int(request.POST['subject2'])
        marks.subject3 = int(request.POST['subject3'])
        marks.subject4 = int(request.POST['subject4'])
        marks.subject5 = int(request.POST['subject5'])
        marks.save()
        return redirect('student_list')
    return render(request, 'students/marks_form.html', {'student': student, 'marks': marks})

def student_search(request):
    result = None
    if request.method == 'POST':
        reg = request.POST.get('register_number', '')
        try:
            student = Student.objects.get(register_number=reg)
            result = student
        except Student.DoesNotExist:
            result = None
    return render(request, 'students/student_search.html', {'result': result})
