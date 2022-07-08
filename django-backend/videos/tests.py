from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from allauth.account.models import EmailAddress


class VideoTest(APITestCase):
    def test(self):
        response_register = self.client.post('/api/users/register/', {'username': 'test',
                                                                      'email': '123@gmail.com',
                                                                      'password1': 'wewe1200',
                                                                      'password2': 'wewe1200'
                                                                      }, format='json')
        t = EmailAddress.objects.get(email='123@gmail.com')
        t.verified = True
        t.save()

        self.client.post('/api/users/register/', {'username': 'test2',
                                                  'email': '1234@gmail.com',
                                                  'password1': 'wewe1200',
                                                  'password2': 'wewe1200'
                                                  }, format='json')
        t = EmailAddress.objects.get(email='1234@gmail.com')
        t.verified = True
        t.save()

        self.assertEqual(response_register.status_code, status.HTTP_201_CREATED)

        response_login = self.client.post('/api/users/login/', {'username': 'test',
                                                                'password': 'wewe1200'
                                                                }, format='json')

        self.assertEqual(response_login.status_code, status.HTTP_200_OK)

        response_invalid_video_post = self.client.post('/api/videos/', {"title": "Тестовое видео",
                                                                        "description": "Test",
                                                                        "video": '',
                                                                        "thumbnail": ''}, format='json')

        self.assertEqual(response_invalid_video_post.status_code, status.HTTP_400_BAD_REQUEST)

        response_like = self.client.post('/api/videos/1/likes', {"is_liked": True}, format='json')

        self.assertEqual(response_like.status_code, status.HTTP_404_NOT_FOUND)

        response_logout = self.client.post('/api/users/logout/', '', format='json')

        self.assertEqual(response_logout.status_code, status.HTTP_200_OK)

        self.client.post('/api/users/login/', {'username': 'test2',
                                               'password': 'wewe1200'
                                               }, format='json')

        response_subscribe = self.client.post('/api/users/1/subscribe', '', format='json')

        self.assertEqual(response_subscribe.status_code, status.HTTP_200_OK)

        response_unsubscribe = self.client.post('/api/users/1/subscribe', '', format='json')

        self.assertEqual(response_unsubscribe.status_code, status.HTTP_200_OK)

        response_password_change = self.client.post('/api/users/password-change/', {'new_password1': 'abiba123',
                                                                                    'new_password2': 'abiba123'
                                                                                    }, format='json')

        self.assertEqual(response_password_change.status_code, status.HTTP_200_OK)

        self.client.post('/api/users/logout/', '', format='json')

        response_newpass_login = self.client.post('/api/users/login/', {'username': 'test2',
                                                                        'password': 'abiba123'
                                                                        }, format='json')

        self.assertEqual(response_newpass_login.status_code, status.HTTP_200_OK)
