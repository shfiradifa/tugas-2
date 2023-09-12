from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appName': 'Firtix',
        'name': 'Shafira Ramadhina Adifa',
        'class': 'PBP-A',
    }

    return render(request, "main.html", context)