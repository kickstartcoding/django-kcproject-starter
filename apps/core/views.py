from django.shortcuts import render

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'home_page.html', context)

def about(request):
    context = {
    }

    return render(request, 'about_page.html', context)

