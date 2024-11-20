import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Views
@login_required(login_url='/login')
def show_main(request):
    productEntries = Product.objects.filter(user=request.user)  # Ambil produk sesuai user
    context = {
        'productEntries': productEntries,
        'nama_pemilik': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Tidak ada data login terakhir'),
    }
    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Ambil gambar dari request.FILES
        user = request.user

        new_product = Product(name=name, price=price, description=description, image=image, user=user)
        new_product.save()

    return HttpResponse(b"CREATED", status=201)

def create_product_entry(request):
    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            # Jika request dari AJAX, kembalikan JSON response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                product_data = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'image_url': product.image.url  # Pastikan `image.url` benar.
                }
                return JsonResponse({'success': True, 'product': product_data}, status=200)

            return redirect('main:show_main')
        
        # Jika tidak valid, kembalikan error response jika AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    context = {'form': form}
    return render(request, 'add_product.html', context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
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

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = ProductEntryForm.objects.create(
            user=request.user,
            mood=data["mood"],
            mood_intensity=int(data["mood_intensity"]),
            feelings=data["feelings"]
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)