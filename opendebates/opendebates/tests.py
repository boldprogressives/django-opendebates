from django.test import TestCase, Client
from django.test.utils import override_settings
from .models import Category

@override_settings(STATICFILES_STORAGE='pipeline.storage.NonPackagingPipelineStorage', PIPELINE_ENABLED=False)
class ViewTest(TestCase):

    def setUp(self):
        ## put all the preconditions for the test here -- e.g. inserting items into the database.
        Category.objects.create(name="category one")

    def test_data(self):
        ## now we have access to the stuff that's been set up in setUp, and can test things that depend on it
        self.assertEqual(Category.objects.filter(name="category one").count(), 1)
        
    def test_test_view(self):
        c = Client()
        response = c.get('/test/')
        self.assertEqual(response.status_code, 200)
