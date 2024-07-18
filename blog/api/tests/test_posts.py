from unittest import skip
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from api.models import SimplePost, SimpleComment

class PostTestCase(APITestCase):

    def setUp(self) -> None:
        self.post_1 = baker.make(SimplePost, title='test_title_1', body='test_body_1')
        self.post_2 = baker.make(SimplePost, title='test_title_2', body='test_body_2')
        baker.make(SimpleComment, post=self.post_1)
        baker.make(SimpleComment, post=self.post_1)
        baker.make(SimpleComment, post=self.post_2)
        baker.make(SimpleComment, post=self.post_2)
        return super().setUp()

    @skip
    def test_posts_list(self):
        url = reverse('v1_posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()
        posts = result.get('posts')
        self.assertEqual(len(posts), 2)

    # @skip
    def test_create_post(self):
        url = reverse('v1_posts')
        response = self.client.post(url, {
            'title': 'test_title',
            'body': 'test_body'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)