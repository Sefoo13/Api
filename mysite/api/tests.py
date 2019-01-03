from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from polls.models import Question
import pdb

class TestQuestionModel(APITestCase):

    def test_question_creation_db(self):
        self.movie = Question(question_text="My entry title", pub_date='2018-12-24T13:45:25Z')
        self.movie.save()
        self.assertEqual(Question.objects.count(), 1)

    def test_question_creation_post(self):
        url = 'http://localhost:8000/api/polls/'
        data = {'question_text': "My entry title",
                'pub_date': '2018-12-24T13:45:25Z'}
        # client = APIClient(enforce_csrf_checks=True)

        response = self.client.post(url, data, format='json')
        self.assertEqual(201, response.status_code)


        # self.assertEqual(response.data, data)
        # self.assertEqual(Question.objects.count(), 2)