from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appName': 'Fir-tix',
        'name': 'Shafira Ramadhina Adifa',
        'class': 'PBP-A',
    }

    return render(request, "main.html", context)