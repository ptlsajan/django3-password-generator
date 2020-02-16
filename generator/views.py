from django.shortcuts import render
from django.shortcuts import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    
    if request.GET.get('specialcharacters'):
        char.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(char)

    return render(request,'generator/password.html',{'password' : thepassword})

def aboutus(request):
    return render(request,'generator/aboutus.html')