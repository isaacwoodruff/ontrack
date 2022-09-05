from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from .forms import UserForm

class SignUpView(FormView):
    template_name = 'users/sign-up.html'
    form_class = UserForm
    success_url = '/profile'

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=self.request.POST['username'],password=self.request.POST['password1'])
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = "Sign In"
        context["page_title"] = page_title
        return context
