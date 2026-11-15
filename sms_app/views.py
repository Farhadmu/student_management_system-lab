from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        age = request.POST["age"]
        dept = request.POST["dept"]
        Student.objects.create(id=id, name=name, age=age, dept=dept)
        return redirect("student_list")

    return render(request, "add_student.html")


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.dept = request.POST["dept"]
        student.save()
        return redirect("student_list")

    return render(request, "edit_student.html", {"student": student})
    
def delete_student(request, id):
    student = get_object_or_404(student, id=id)
    