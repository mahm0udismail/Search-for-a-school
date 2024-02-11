from django.shortcuts import render

from .forms import FORMStudent
# Create your views here.

def indexStudent(request): 
    if request.method=='POST':
        form = FORMStudent(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
    else:
        form = FORMStudent()
    
    context={'form':form}
    return render(request, 'indexStudent.html' ,context)