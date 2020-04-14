from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from .models import Course


class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'nome': 'Fulano de tal', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

