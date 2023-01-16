from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from sendgrid.helpers.mail import SandBoxMode, MailSettings

User = get_user_model()


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             messages.success(request, f'Hi {username}, Your account has been created! You are now able to log in')
#             return redirect('product_list')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})



def register(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("password2")
        username = email.split('@')[0]

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("product_list")
            # elif User.objects.filter(username=username).exists():
            #     messages.info(request, "Username is taken already")
            #     return redirect("signup")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                mydict = {'username': username}
                html_template = 'accounts/index.html'
                html_message = render_to_string(html_template, context=mydict)
                subject = 'Welcome to SuperMart'
                email_from = settings.DEFAULT_FROM_EMAIL
                recipient_list = [email]
                message = EmailMessage(subject, html_message,
                                    email_from, recipient_list)
                message.content_subtype = 'html'
                message.send()
                messages.success(request, f"Hi {email}, your account has been created, Kindly login below")
                return redirect("login")
        else:
            messages.info(request, "Password do not match")
            return redirect("signup")
    return render(request, "accounts/register2.html")



# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect("product_list")
#         else:
#         
#     messages.info(request, "Credentials Invalid")
#             return redirect("login")

#     else:
#         return render(request, "accounts/login.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        username = User.objects.get(email=email.lower()).username
        print(username)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("product_list")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")

    else:
        return render(request, "accounts/login.html")


def login3(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if "@" in email:
            print("True")
            username = User.objects.get(email=email.lower()).username
            user = auth.authenticate(username=username, password=password)
        else:
            user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("product_list")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")

    else:
        return render(request, "accounts/login3.html")




def logout(request):
    auth.logout(request)
    return redirect("product_list")

   