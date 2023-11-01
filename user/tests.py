from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a sample user for testing
        self.user = CustomUser.objects.create(
            email="test@example.com",
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            username="johndoe",
            nationality="US",
            birthdate="2000-01-01",
            marital_status="SINGLE",
            gender="MALE",
            is_email_verified=True,
            verification_status="VERIFIED",
            nid_number="1234567890"
        )
        
    def test_user_creation(self):
        # Test if the user was created correctly
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.phone_number, "1234567890")
        self.assertEqual(self.user.username, "johndoe")
        self.assertEqual(self.user.nationality, "US")
        self.assertEqual(self.user.birthdate, "2000-01-01")
        self.assertEqual(self.user.marital_status, "SINGLE")
        self.assertEqual(self.user.gender, "MALE")
        self.assertTrue(self.user.is_email_verified)
        self.assertEqual(self.user.verification_status, "VERIFIED")
        self.assertEqual(self.user.nid_number, "1234567890")

    def test_user_str_method(self):
        # Test the __str__ method of the user model
        self.assertEqual(str(self.user), "test@example.cm")

    def test_default_values(self):
        # Test the default values for is_active, is_staff, and is_superuser
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_username_field(self):
        # Test the USERNAME_FIELD attribute
        self.assertEqual(self.user.USERNAME_FIELD, "email")

    def test_verbose_names(self):
        # Test the verbose_name and verbose_name_plural attributes
        self.assertEqual(self.user._meta.verbose_name, "user")
        self.assertEqual(self.user._meta.verbose_name_plural, "users")

