from django.test import TestCase

from api_instagram.models import Photo

from api_instagram.models import User


class PhotoTestCase(TestCase):
    def setUp(self):
        new_user = User.objects.create(username='ccbndh')
        temp_user = User.objects.create(username='temp')
        Photo.objects.create(user=new_user, title='watch')
        Photo.objects.create(user=new_user, title='hot girl')
        Photo.objects.create(user=temp_user, title='hot girl')

    def test_number_photo_user_uploaded(self):
        """User ccbndh should have 2 photo uploaded"""

        photo_of_user_ccbn = Photo.objects.filter(user__username='ccbndh')
        self.assertEqual(photo_of_user_ccbn.count(), 2)
