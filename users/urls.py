from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import SignIn

from . import views

urlpatterns = [
   path('', LoginView.as_view(
            extra_context={
                'page_title':'Sign In'
            },
            authentication_form=SignIn,
            template_name='users/sign-in.html',
            redirect_authenticated_user=True),
        name='sign_in'),
    path('sign-up', views.SignUpView.as_view(), name='sign_up'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('profile/', login_required(TemplateView.as_view(template_name="users/profile.html")), name='profile'),
    path('sign-out', views.logout_view, name='logout'),
    path('delete-profile', views.UserDeleteView.as_view(), name='delete_profile'),
]
