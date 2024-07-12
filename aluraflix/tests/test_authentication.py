from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_correta(self):
        """Teste que verifica a autenticação de um usuário com as credenciais corretas."""
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_username_incorreto(self):
        """Teste que verifica se o nome de usuário foi digitado corretamente."""
        user = authenticate(username='c3pp', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_password_incorreto(self):
        """Teste que verifica se a senha foi digitada corretamente."""
        user = authenticate(username='c3po', password='12345')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_autorizada(self):
        """Teste que verifica uma requisição GET de um usuário autenticado."""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)