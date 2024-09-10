from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'camera',
        'price': 'RP. 100.000.000,00',
        'description': 'belibelibeli',
        'image' : 'https://images.unsplash.com/photo-1721332153282-3be1f363074d?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'nama_toko' : 'Palugada',
        'nama_pemilik' : 'Micheline Wijaya Limbergh',
        'kelas_pemilik' : 'PBP D'
    }

    return render(request, "main.html", context)