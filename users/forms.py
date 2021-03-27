from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter your email')
    full_name = forms.CharField(required=True, help_text='Enter your full name')
    phone = forms.CharField(required=True, max_length=10, help_text='Enter your phone number')
    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     for fieldname in ['username', 'email', 'full_name', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None
            
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone', 'password1', 'password2']
