from django.test import TestCase
from django.urls import reverse
from .models import Books
# Create your tests here.

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Books.objects.create(
        title="my life",
        subtitle="horror",
        author="ankit",
        isbn="4444444444444",
        )
    def test_book_content(self):
        self.assertEqual(self.book.title, "my life")
        self.assertEqual(self.book.subtitle, "horror")
        self.assertEqual(self.book.author, "ankit")
        self.assertEqual(self.book.isbn, "4444444444444")

    def test_book_listview(self):
        response = self.client.get(reverse("Home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "horror")
        self.assertTemplateUsed(response, "books/books_list.html")