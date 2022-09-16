from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, EmailField, CharField
from users.models import Profile

class UserForm(UserCreationForm):
    '''
    UserForm extends the UserCreationForm and customizes it with fields specified in Meta.
    The form is then styled on the backend with crispy_forms
    '''
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'mt-5'
        self.helper.form_method = 'post'
        self.helper.form_group_wrapper_class = 'form-group'
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('first_name'),
                    css_class='me-md-4'
                ),
                Field('last_name'),
                css_class='d-md-flex'
            ),
            Field('username'),
            Field('email'),
            Field('password1'),
            Field('password2'),
            Submit('submit', 'Sign Up', css_class='button white w-100'),
        )

class SignIn(AuthenticationForm):
    '''
    SignIn form extends the AuthenticationForm and customizes the styling 
    on the backend with crispy_forms
    '''
    class Meta:
        model = User
        fields = ["username", "password"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'mt-5'
        self.helper.form_method = 'post'
        self.helper.form_group_wrapper_class = 'form-group'
        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
            Submit('submit', 'Sign Up', css_class='button white w-100'),
        )

class UserUpdateForm(ModelForm):
    email = EmailField(required=False)
    username = CharField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

class EditProfileForm(ModelForm):
    '''
    This form is created from fields in the Profile model
    '''
    class Meta:
        model = Profile
        fields = ["github", "job_title", "avatar"]

