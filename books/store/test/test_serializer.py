from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='book1', author_name='Author 1', price=1200)
        book_2 = Book.objects.create(name='book2', author_name='Author 2', price=500)
        book_3 = Book.objects.create(name='book3', author_name='Author 3', price=560)

        data = BookSerializer([book_1, book_2, book_3], many=True).data

        expected_data = [
            {
                'id': book_1.id,
                'name': 'book1',
                'price': '1200.00',
                'author_name': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': 'book2',
                'price': '500.00',
                'author_name': 'Author 2'
            },
            {
                'id': book_3.id,
                'name': 'book3',
                'price': '560.00',
                'author_name': 'Author 3'
            }
        ]
        self.assertEqual(expected_data, data)
