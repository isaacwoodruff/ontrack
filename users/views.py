from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from .forms import UserForm

class SignUpView(FormView):
    '''
    Class based sign up view that displays the crispy UserForm built in forms.py
    If the form is valid, it saves a new user to the database, then the user is logged in
    '''
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
