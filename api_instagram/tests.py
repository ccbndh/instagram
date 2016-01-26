from django.test import TestCase


# Create your tests here.
class SimpleTestCase(TestCase):
    def test_simple(self):
        self.assertEquals(1 + 1, 2)
        self.assertEquals(1 + 1, 3)
