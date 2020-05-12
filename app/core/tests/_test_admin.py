from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# from .model


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='super@user.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)

        # self.user = get_user_model().objects.create_user(
        #     email='test@test.com',
        #     password='testPass123',
        #     name='Test User Full Name'
        # )
        # # self.user2 = get_user_model().objects.create_user(
        #     email='user2@user.com',
        #     password='123password',
        #     name='second user'
        # )

    def test_users_listed(self):
        '''
        Test users are listed in users page.
        '''
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # self.assertContains(res, self.user.name)
        # self.assertContains(res, self.user2.email)
        # self.assertContains(res, self.user.name)
        # self.assertContains(res, self.user2.email)
