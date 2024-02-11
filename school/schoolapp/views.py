from django.shortcuts import render
from .models import School 
from .forms import FORMSchool
from .filters import SchoolFilter


# Create your views here.


def index(request):
    filter = SchoolFilter(request.GET, queryset=School.objects.all())
    return render(request, 'index.html' ,{'filter': filter})