from django.shortcuts import render, redirect
from .forms import ContactForm, RegisterForm

from django.contrib.auth import get_user_model
User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)

def home_page(request):
    if request.user.is_authenticated:
        return render(request, "home_page.html")
    else:
        return redirect(request, "home_page.html")

def contact_page(request):
    contact_form = ContactForm()

    context = {
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST.get('fullname'))
    return render(request,"contact/contact.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)

