from multiprocessing import context
from django.shortcuts import render
from kategoriapp.models import user
# Create your views here.
def kategori(request):
    datamap = user.objects.all()
    return render(request,'kategori.html',{'data':datamap})