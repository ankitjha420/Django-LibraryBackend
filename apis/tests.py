from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Books

class ApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Books.objects.create(
            title = "my life",
            subtitle = "horror",
            author = "myself",
            isbn = "5555555555555"
        )
    def test_api_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.count(), 1)
        self.assertContains(response, self.book)