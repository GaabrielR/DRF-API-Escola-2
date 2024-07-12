from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verificar_carregamento(self):
        """Teste que verifica o carregamento do arquivo JSON."""
        programa_bizarro = Programa.objects.get(pk=1)
        todos_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_programas), 9)