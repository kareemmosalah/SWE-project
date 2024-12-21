from django.test import TestCase
from myapp.forms import CustomUserCreationForm
class CustomUserCreationFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
            'is_player': True
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_invalid_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'differentpassword',
            'is_player': True
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())