from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Es Kopi Susu Tetangga',
        'description': 'Perpaduan iced latte dan creamer dengan campuran gula aren',
        'amount': 15,
    }

    return render(request, "main.html", context)