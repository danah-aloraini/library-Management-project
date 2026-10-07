from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms



class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get("username")
        password = cleaned.get("password")
        confirm = cleaned.get("confirm")

        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")

        if password and len(password) > 20:
            raise forms.ValidationError("Password must be at most 20 characters.")

        if password != confirm:
            raise forms.ValidationError("Error! Passwords must match.")

        return cleaned


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # unique Username
            if User.objects.filter(username=username).exists():
                return render(request, "accounts/register.html", {
                    "form": form,
                    "message": "Username already taken."
                })

            # create user
            user = User.objects.create_user(username, email, password)
            user.save()

            login(request, user)
            return HttpResponseRedirect(reverse("accounts:login_view"))
        else:
            return render(request, "accounts/register.html", {"form": form})

    return render(request, "accounts/register.html", {"form": RegisterForm()})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("accounts:login_view"))# replace ofter bulding view books return HttpResponseRedirect(reverse("books:index"))
            else:
                return render(request, "accounts/login.html", {
                    "form": form,
                    "message": "Error: you need to register first"
                })
        else:
            return render(request, "accounts/login.html", {"form": form})

    return render(request, "accounts/login.html", {"form": LoginForm()})


