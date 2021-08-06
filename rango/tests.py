from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.views import get_user_model
from .models import Category, Page

# Create your tests here.

class IndexTest(TestCase):
    def test_index_view(self):
        url = reverse('rango:add_category')
        get_user_model().objects.create_user('yajing', password='123456sad')
        data = {
            'name': 'category',
            'views': 0,
            'likes': 0
        }
        res = self.client.login(username='yajing', password='123456sad')

        res = self.client.post(url, data=data)
        c = Category.objects.filter(name='category').count()
        self.assertEqual(c, 1, f"When adding a new category, it does not appear in the list of categories after being created. Check your add_category() view as the start of a debugging point.")

    def test_index_view_get(self):
        url = reverse('rango:add_category')
        get_user_model().objects.create_user('yajing', password='123456sad')
        data = {
            'name': 'category',
            'views': 0,
            'likes': 0
        }
        res = self.client.login(username='yajing', password='123456sad')
        res = self.client.get(url)
        self.assertTrue('add a category' in res.content.decode().lower())


class AddPageTestCase(TestCase):

    def test_add_page_view(self):  
        category = Category.objects.create(name='category', views=0, likes=0, slug=1)
        url = reverse('rango:add_page', kwargs={'category_name_slug': category.slug})
        get_user_model().objects.create_user('yajing', password='123456sad')
        data = {
            'title': 'page',
            'url': 'http://github.com',
            'views': 0
        }
        res = self.client.login(username='yajing', password='123456sad')
        res = self.client.post(url, data=data)
        c = Page.objects.filter(title='page').count()
        self.assertEqual(c, 1, f"When adding a new page, it does not appear in the list of categories after being created. Check your add_category() view as the start of a debugging point.")

    def test_add_page_view_get(self):
        category = Category.objects.create(name='category', views=0, likes=0, slug=1)
        url = reverse('rango:add_page', kwargs={'category_name_slug': category.slug})
        get_user_model().objects.create_user('yajing', password='123456sad')
        data = {
            'title': 'page',
            'url': 'http://github.com',
            'views': 0
        }
        res = self.client.login(username='yajing', password='123456sad')
        res = self.client.get(url)
        self.assertTrue('add a page' in res.content.decode().lower())

class UploadPictureTestCase(TestCase):

    def test_upload_picture_view(self):
        
        user = get_user_model().objects.create_user('yajing', password='123456sad')
        url = reverse('rango:profile', kwargs={'username': 'yajing'})
        res = self.client.login(username='yajing', password='123456sad')
        with open('media/cat.jpg') as f:
            data = {
                'website': 'http://github.com',
                'picture': f.read()
            }
            self.client.post(url, data=data)
        print(user)
        self.assertIsNotNone(user.userprofile)


class ChangePasswordTestCase(TestCase):
    def test_change_password(self):
        user = get_user_model().objects.create_user('yajing', password='123456sad')
        url = reverse('auth_password_change')
        res = self.client.login(username='yajing', password='123456sad')
        data = {
            'old_password' : '123456sad',
            'new_password1' : '123sad',
            'new_password2' : '123sad',
        }
        r = self.client.post(url, data=data)
        print(r.content.decode())
        res = self.client.login(username='yajing', password='123sad')
        self.assertTrue(res)