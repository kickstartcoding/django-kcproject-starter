from django.shortcuts import render

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'page/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'page/about.html', context)

