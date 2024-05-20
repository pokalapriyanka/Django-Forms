from django.shortcuts import render
from app.forms import *
# Create your views here.

def school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    return render(request,'school.html',d)