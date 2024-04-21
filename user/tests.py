from django.test import TestCase, Client
from .models import UserRegistration
from .serializers import UserRegistrationSerializer
from django.urls import reverse

User = UserRegistration


# Create your tests here.
class UserRegistrationTest(TestCase):
    def test_str(self):
        item = UserRegistration.objects.create(
            username="AmyO",
            email="amy@gmail.com",
            password="AmyOffor#1",
        )
        itemstr = item.__str__()

        self.assertEqual(itemstr, "AmyO")


class UserRegistrationLoginTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'Test#User001'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_user_login(self):
        User.objects.create(username=self.username, email=self.email, password=self.password)

        # Log in the test user
        response = self.client.post(
            ('/user/login/'),  # Replace 'user-login' with your login view's URL name
            data={'username': self.username, 'password': self.password},
        )

        # Assert that the user was logged in successfully
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json())
        self.assertTrue('refresh' in response.json())


class EmailValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuseremail.com'
    password = 'Test#User001'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], ['Enter a valid email address.'])


class PasswordLengthValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'Test#User'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'], ["Password should have at least 10 characters."])


class PasswordUpperCaseValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'test#user123'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'], ["Password should contain at least 1 uppercase character."])


class PasswordLowerCaseValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'TEST#USER123'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'], ["Password should contain at least 1 lowercase character."])


class PasswordDigitValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'Test#Userss'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'], ["Password should contain at least 1 digit."])


class PasswordSpecialCharacterValidationTestCase(TestCase):

    # Create a test user
    username = 'testuser'
    email = 'testuser@email.com'
    password = 'Test123Userss'

    def test_user_registration(self):
        response = self.client.post(
            ('/user/register/'),  # Replace 'user-registration' with your registration view's URL name
            data={'username': self.username, 'email': self.email, 'password': self.password},
        )

        # Assert that the user was created successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'], ["Password should have at least 1 special characters."])
