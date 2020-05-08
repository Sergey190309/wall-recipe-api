from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        '''
        Thes creating a new user with email successfull.
        '''
        email = 'test@test.com'
        password = 'testPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''
        Test whether user's email normalized ie written in lower case.
        '''
        email = 'test@TeSt.com'
        password = 'testPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''
        Test creating user with no e-mail raise the error.
        '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='kkkkk'
            )

    def test_create_new_superuser(self):
        '''
        Test whether your are creating superuser.
        '''
        user = get_user_model().objects.create_superuser(
            'test@superuser.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
