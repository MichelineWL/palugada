from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def show_main(request):
    product = Product.objects.all()

    context = {
        'name' : 'Camera',
        'price': 'RP. 100.000.000,00',
        'description': 'Produk ini merupakan produk pilihan customer. Kamera tersebut menghasilkan jenjang warna foto yang hidup disertai dengan ...',
        'image' : 'https://images.unsplash.com/photo-1721332153282-3be1f363074d?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'nama_toko' : 'Palugada',
        'nama_pemilik' : 'Micheline Wijaya Limbergh',
        'kelas_pemilik' : 'PBP D',
        'product_entries' : product,
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None, request.FILES or None)  # Include request.FILES

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, 'add_product.html', context)

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# membuat fungsi post yang biasanya ada di service.js
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been succesfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)