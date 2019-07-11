from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request=request, data=request.POST)
        if form.is_valid():
            form.save()

            # Uncomment this if you want sign-ups to be able to log-in right
            # away:
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('log_in')
    else:
        form = UserCreationForm(request=request)

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
#
