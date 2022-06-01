from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account Created For {username}.')
            return redirect('index')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)
