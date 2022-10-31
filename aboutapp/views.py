from multiprocessing import context
from django.shortcuts import render
# Create your views here.

def about(request):
    context = {
        'about' : 'Tentang Kami'
    }
    return render(request,'about.html',context)