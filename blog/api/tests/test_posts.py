from unittest import skip
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.testcases import override_settings
from django.contrib.auth.models import User
from model_bakery import baker

from api.models import SimplePost, SimpleComment, UserStatus


class PostTestCase(APITestCase):

    def setUp(self) -> None:
        self.post_1 = baker.make(SimplePost, title='test_title_1', body='test_body_1', like=10)
        self.post_2 = baker.make(SimplePost, title='test_title_2', body='test_body_2', like=20)
        baker.make(SimpleComment, post=self.post_1)
        baker.make(SimpleComment, post=self.post_1)
        baker.make(SimpleComment, post=self.post_2)
        baker.make(SimpleComment, post=self.post_2)
        self.user_1 = User.objects.create_user(username='user_1', password='pass_1')
        self.user_1_status = baker.make(UserStatus, user=self.user_1, is_active=True)
        self.token_1 = self.get_token()
        return super().setUp()

    def get_token(self):
        url = reverse('auth')
        response = self.client.post(url, {
            'username': self.user_1.username,
            'password': 'pass_1'
        })
        result = response.json()
        return result.get('token')


    def do_request(self, url, method, data=None, auth=True):
        headers = {}
        if auth:
            headers['Authorization'] = f"Token {self.token_1}"
        if method == 'get':
            return self.client.get(url, data, headers=headers)
        else:
            return self.client.put(url, data, headers=headers)

    @skip
    def test_get_token(self):
        url = reverse('auth')
        response = self.client.post(url, {
            'username': self.user_1.username,
            'password': 'pass_1'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()
        self.assertIn('token', result)

    @skip
    def test_posts_list(self):
        url = reverse('v3_posts-list')
        response = self.do_request(url, 'get', auth=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.json().get('results')
        self.assertEqual(len(posts), 2)

    # @skip
    def test_create_post(self):
        url = reverse('v3_posts-list')
        response = self.client.post(url, {
            'title': 'test_title',
            'body': 'test_body'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @skip
    def test_get_post(self):
        url = reverse('v3_posts-detail', kwargs={
            'pk': self.post_1.pk
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @skip
    def test_get_last_post(self):
        url = reverse('v3_posts-last-post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @skip
    def test_filter_title_post(self):
        url = reverse('v3_posts-list')
        response = self.client.get(url, data={'title': 'test_title_1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.json()
        self.assertEqual(len(posts), 1)

    @skip
    def test_filter_like_post(self):
        url = reverse('v3_posts-list')
        response = self.client.get(url, data={'like__gt': 11})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.json()
        self.assertEqual(len(posts), 1)

    @skip
    def test_search_post(self):
        url = reverse('v3_posts-list')
        response = self.client.get(url, data={'search': 'body_2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = response.json()
        self.assertEqual(len(posts), 1)

    @skip
    def test_pagination(self):
        for i in range(10):
            baker.make(SimplePost, title=f'test_title_{i}')

        url = reverse('v3_posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        page_1_posts = response.json()
        page_1_posts_ids = [item.get('id') for item in page_1_posts.get('results')]
        next_url = page_1_posts.get('next')
        baker.make(SimplePost, title=f'test_title_1000')
        response = self.client.get(next_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        page_2_posts = response.json()
        page_2_posts_ids = [item.get('id') for item in page_2_posts.get('results')]
        common_ids = list(set(page_1_posts_ids).intersection(list(page_2_posts_ids)))
        self.assertEqual(len(common_ids), 0)
