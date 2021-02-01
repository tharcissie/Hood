from django.test import TestCase
from  .models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='tharcissie', password='qwewe')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class hoodTest(TestCase):
    def setup(self):
        self.user = User.objects.create(id=a, username='tharcissie')
        self.hood = Hood.objects.create(id=1, name='kabuga', location='kigali',image='a.jpg', police=123, health=119 )

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))

    def create_hood(self):
        self.hood.create_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_get_hoods(self):
        self.hood.save()
        hoods = hood.all_hoods()
        self.assertTrue(len(hoods) > 0)

    def test_search_hood(self):
        self.hood.save()
        hood = hood.search_hood('test')
        self.assertTrue(len(hood) > 0)

    def test_delete_hood(self):
        self.hood.delete_hood()
        hood = hood.search_hood('test')
        self.assertTrue(len(hood) < 1)



