from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Hi {username}, Your account has been created! You are now able to log in')
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register2.html', {'form': form})


