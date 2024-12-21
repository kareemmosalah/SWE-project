#test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
class UserViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )
        self.client.login(username='testuser', password='testpass123')
    def test_change_username_success(self):
        response = self.client.post(reverse('change_username'), {'new_username': 'newtestuser'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newtestuser')
        self.assertRedirects(response, reverse('user_profile'))
    def test_change_username_duplicate(self):
        get_user_model().objects.create_user(username='existinguser', password='testpass123')
        response = self.client.post(reverse('change_username'), {'new_username': 'existinguser'})
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.username, 'existinguser')
        self.assertContains(response, "This username is already taken.")