from django.shortcuts import render
from .forms import UserForm

def sign_in(request):
    context = {
        "page_title": "Sign In",
    }
    return render(request, 'users/sign-in.html', context)

def sign_up(request):
    form = UserForm()
    context = {
        "page_title": "Sign In",
        "form": form,
    }
    return render(request, 'users/sign-up.html', context)
