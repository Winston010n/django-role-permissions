from django.urls import reverse
from rest_framework.test import APITestCase

from .models import CustomUser


class RolePermissionEndpointTests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_user(
            username="admin",
            password="test-password",
            role=CustomUser.Role.ADMIN,
        )
        self.moderator = CustomUser.objects.create_user(
            username="moderator",
            password="test-password",
            role=CustomUser.Role.MODERATOR,
        )
        self.user = CustomUser.objects.create_user(
            username="user",
            password="test-password",
            role=CustomUser.Role.USER,
        )

    def test_admin_panel_allows_only_admin(self):
        url = reverse("admin-panel")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        for account in (self.moderator, self.user):
            with self.subTest(role=account.role):
                self.client.force_authenticate(user=account)
                self.assertEqual(self.client.get(url).status_code, 403)

        self.client.force_authenticate(user=self.admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Добро пожаловать в панель администратора!"},
        )

    def test_user_dashboard_allows_only_regular_users(self):
        url = reverse("user-dashboard")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        for account in (self.admin, self.moderator):
            with self.subTest(role=account.role):
                self.client.force_authenticate(user=account)
                self.assertEqual(self.client.get(url).status_code, 403)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Личный кабинет пользователя"})
