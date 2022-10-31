from django.shortcuts import render

def product(request):
    context = {
        'judul': 'Produk Muslim Store',
    }
    return render(request,'product.html',context)