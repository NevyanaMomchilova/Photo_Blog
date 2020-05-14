from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms


def sign_up(request):
    if request.method == "POST":
        form = forms.UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been successfully created. You are now able to log in.")
            return redirect("login")
    else:
        form = forms.UserSignUpForm()
    return render(request, "users/sign_up.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")

