from django.test import TestCase
from django.test import SimpleTestCase

from pages.models import ArchiveAudio, ArchivePhoto, ArchiveVideo

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):

        response = self.client.get('/archivesHome/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):

        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)

class ArchivePhotoModelTest(TestCase):
    def setUp(self):
        ArchivePhoto.objects.create(title='just a test', media="just a test also")

    def test_text_content(self):
        archive=ArchivePhoto.objects.get(id=1)
        expected_object_name = f'{archive.title}'
        self.assertEqual(expected_object_name, 'just a test')

class ArchiveAudioModelTest(TestCase):
    def setUp(self):
        ArchiveAudio.objects.create(title='just a test', media="just a test also")

    def test_text_content(self):
        archive=ArchiveAudio.objects.get(id=1)
        expected_object_name = f'{archive.title}'
        self.assertEqual(expected_object_name, 'just a test')

class ArchiveVideoModelTest(TestCase):
    def setUp(self):
        ArchiveVideo.objects.create(title='just a test', media="just a test also")

    def test_text_content(self):
        archive=ArchiveVideo.objects.get(id=1)
        expected_object_name = f'{archive.title}'
        self.assertEqual(expected_object_name, 'just a test')