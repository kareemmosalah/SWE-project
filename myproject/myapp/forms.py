# myproject/myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, initial=False)
    is_player = forms.BooleanField(required=False, initial=False)
    is_court_owner = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_player', 'is_court_owner')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = self.cleaned_data.get('is_admin', False)
        user.is_player = self.cleaned_data.get('is_player', False)
        user.is_court_owner = self.cleaned_data.get('is_court_owner', False)
        if commit:
            user.save()
        return user


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        
class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))