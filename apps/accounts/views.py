from django.shortcuts import render

def log_in(request):

    context = {
    }

    return render(request, 'home_page.html', context)

def sign_up(request):
    context = {
    }

    return render(request, 'about_page.html', context)

