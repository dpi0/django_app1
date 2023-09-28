from django.shortcuts import render, redirect

# from django.contrib.auth.models import User

# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ..forms import UserCreationForm
from ..models import User


def login_view(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "email or password is incorrect")

    context = {"page": page}

    return render(request, "main_app/login_and_register.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(
                request, "An error occurred during registration"
            )

    context = {"form": form}

    return render(request, "main_app/login_and_register.html", context)
