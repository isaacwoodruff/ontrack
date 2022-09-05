from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign-up', views.SignUpView.as_view(), name='sign_up'),
]
