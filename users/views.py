from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserForm

def sign_in(request):
    context = {
        "page_title": "Sign In",
    }
    return render(request, 'users/sign-in.html', context)

class SignUpView(FormView):
    template_name = 'users/sign-up.html'
    form_class = UserForm
    success_url = '/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = "Sign In"
        context["page_title"] = page_title
        return context
