from django.db import connection
from django.test import TestCase


class BootstrapSmokeTest(TestCase):
    def test_database_connection(self) -> None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
        self.assertEqual(row, (1,))
