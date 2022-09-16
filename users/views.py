from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm, EditProfileForm, UserUpdateForm
from django.contrib.auth.models import User

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def edit_profile(request):
    if request.method == 'POST':
        print("form POSTed")
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_form = EditProfileForm(data=request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            print("Form is valid")
            user_form.save(commit=False)
            user_form.email = user_form.cleaned_data.get("email")
            user_form.username = user_form.cleaned_data.get("username")
            user_form.save()
            profile_form.save()
            print(request.user)
        redirect('edit_profile')
    
    else:
        profile_form = EditProfileForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/edit-profile.html', {'profile_form': profile_form, 'user_form': user_form,})
