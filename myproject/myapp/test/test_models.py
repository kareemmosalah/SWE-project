from django.test import TestCase
from myapp.models import Court, CustomUser
class CourtModelTests(TestCase):
    def test_create_court(self):
        court = Court.objects.create(
            name='Test Court',
            details='Test details',
            pricing='100',
            location='Test Location',
            contact_phone='1234567890',
            contact_email='test@example.com',
            reviews=4.5,
            city='Test City'
        )
        self.assertEqual(court.name, 'Test Court')
        self.assertEqual(court.city, 'Test City')
        
class CustomUserModelTests(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertEqual(user.email, 'testuser@example.com')