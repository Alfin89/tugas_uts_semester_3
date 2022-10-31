from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'judul': 'Home Muslim Store',
    }
    return render(request,'index.html',context)
