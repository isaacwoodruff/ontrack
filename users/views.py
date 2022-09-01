from django.shortcuts import render

def sign_in(request):
    context = {
        "page_title": "Sign In",
    }
    return render(request, 'users/sign-in.html', context)

def sign_up(request):
    context = {
        "page_title": "Sign Up",
    }
    return render(request, 'users/sign-up.html', context)
