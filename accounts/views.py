from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


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
    return render(request, 'accounts/register.html', {'form': form})



def register2(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("product_list")
            # elif User.objects.filter(username=username).exists():
            #     messages.info(request, "Username is taken already")
            #     return redirect("signup")
            else:
                user = User.objects.create_user(email=email, password=password1)
                user.save()
                messages.success(request, f"Hi {email}, your account has been created")
                return redirect("product_list")
        else:
            messages.info(request, "Password do not match")
            return redirect("signup")
    return render(request, "accounts/register2.html")





