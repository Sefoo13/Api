from rest_framework.test import APITestCase
from polls.models import Question
import pdb


class TestQuestionModel(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/api/polls/'
        self.url_question = 'http://localhost:8000/api/polls/1/'
        self.name = "My entry title"
        self.new_name = "Update entry title"
        self.date = "2018-12-24T13:45:25Z"

        data = {'question_text': self.name,
                'pub_date': self.date,
                '_content_type': "application/json"}
        self.response = self.client.post(self.url, data, format='json')

    def test_question_creation_db(self):
        self.movie = Question(question_text=self.name, pub_date=self.date)
        self.movie.save()
        self.assertEqual(Question.objects.count(), 2)

    def test_question_creation_post(self):
        self.assertEqual(201, self.response.status_code)

    def test_get_created_question(self):
        get_question = self.client.get(self.url, format="json")
        # pdb.set_trace()
        self.assertEqual(get_question.data["count"], 1)

    def test_update_question(self):
        get_name = self.client.get(self.url_question, format="json")
        self.assertEqual(self.name, get_name.data['question_text'])
        response_put = self.client.put(self.url_question, {
            'question_text': self.new_name,
            'pub_date': self.date,
            'pk': 1
        }, format="json")
        # pdb.set_trace()
        self.assertEqual(self.new_name, response_put.data['question_text'])


