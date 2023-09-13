from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appName': 'Tawa Riang Candu',
        'appDesc': 'Aplikasi pemesanan tiket untuk pertunjukan teater musikal yang mengadaptasi serial film Upin & Ipin, menghadirkan pengalaman tontonan yang penuh tawa dan candu bagi penggemar.',
        'name': 'Shafira Ramadhina Adifa',
        'class': 'PBP-A',
    }

    return render(request, "main.html", context)