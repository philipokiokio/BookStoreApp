from .views import HomePageView
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from. views import HomePageView,AboutPageView

# Create your tests here.



class HomepageTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        
        self.assertEqual(self.response.status_code, 200)


    def test_homepage_url_new(self):
        
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        
        self.assertTemplateUsed(self.response, 'home.html')


    def test_homepage_contain_correct_html(self):
        
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        
        self.assertNotContains(self.response, 'hi this is also a test.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
        view.func.__name__,HomePageView.as_view().__name__)

class AboutpageTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        
        self.assertEqual(self.response.status_code, 200)


    def test_aboutpage_url_new(self):
        
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        
        self.assertTemplateUsed(self.response, 'about.html')


    def test_aboutpage_contain_correct_html(self):
        
        self.assertContains(self.response, 'About')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        
        self.assertNotContains(self.response, 'hi this is also a test.')

    def test_aboutpage_url_resolves_homepageview(self):
        view = resolve('/about/')
        self.assertEqual(
        view.func.__name__,AboutPageView.as_view().__name__)        