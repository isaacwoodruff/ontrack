from django.shortcuts import render

def login(request):
    context = {
        "page_title": "Login",
    }
    return render(request, 'users/login-signup.html', context)
