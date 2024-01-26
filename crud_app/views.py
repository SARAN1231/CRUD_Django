from django.shortcuts import render,redirect
from crud_app.models import student
from crud_app.forms import StudentForm
# Create your views here.
def studentclass(request):
    studata = student.objects.all()
    return render(request,'CRUD_APP/index.html' ,{"studetails":studata})


def  createstu(request):
    form = StudentForm()
    if(request.method =='POST'):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save() # save the user entered datas in DB
            return redirect('/crud_app/student')
    return render(request,'CRUD_APP/form.html' ,{'form':form})


def deletestu(request,id):
    students = student.objects.get(id=id)
    students.delete()
    return redirect('/crud_app/student')

def updatestu(request,id):
    students = student.objects.get(id=id)
    form = StudentForm()
    if(request.method =='POST'):
        form=StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save() # save the user entered datas in DB
            return redirect('/crud_app/student')
    return render (request,'CRUD_APP/update.html' ,{'student':students})
    