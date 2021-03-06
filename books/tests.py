from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, Review




# Create your tests here.
class BookTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = 'reviewuser',
            email = 'reviewuser@user.use',
            password =  'testpass123'
        )

        self.book = Book.objects.create(title = 'Harry Potter',
                                        author = 'JK Rowling',
                                        price = '25.00')

        self.review = Review.objects.create(
            book =self.book,
            author = self.user,
            review = 'an excellent review'
        )


    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')


    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')



    def test_book_detail_view(self):
        self.client.login(
            email='reviewuser@email.com',
            password = 'testuser123'
        )
        # self.user.user_permissions.add(self.special_permission)
        # self.user.user_permissions.add(self.special_permission)  
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/123345/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(no_response.status_code, 404)
        # self.assertContains(response, 'Harry Potter')
        # self.assertContains(response, 'an excellent review')
        # self.assertTemplateUsed(response, 'books/book_detail.html')
    