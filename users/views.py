from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError


def register_view(request):
    try:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully!")
                return redirect("users:profile")
            else:
                messages.error(request, "Please fix the errors below.")
        else:
            form = CustomUserCreationForm()
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        form = CustomUserCreationForm()
    except Exception as e:
        messages.error(request, f"Unexpected error: {e}")
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect("users:profile")
            else:
                messages.error(request, "Invalid username or password.")
    except Exception as e:
        messages.error(request, f"Unexpected error: {e}")

    return render(request, "users/login.html")


@login_required
def profile_view(request):
    try:
        user = request.user
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully!")
                return redirect("users:profile")
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = CustomUserChangeForm(instance=user)
    except DatabaseError as e:
        messages.error(request, f"Database error: {e}")
        form = CustomUserChangeForm(instance=request.user)
    except Exception as e:
        messages.error(request, f"Unexpected error: {e}")
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "users/profile.html", {"form": form})


def logout_view(request):
    try:
        logout(request)
        messages.info(request, "Logged out successfully.")
    except Exception as e:
        messages.error(request, f"Unexpected error: {e}")
    return redirect("users:login")
