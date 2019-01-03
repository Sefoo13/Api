from rest_framework.test import APITestCase
from polls.models import Question
import pdb


class TestQuestionModel(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/api/polls/'
        data = {'question_text': "My entry title",
                'pub_date': "2018-12-24T13:45:25Z",
                '_content_type': "application/json"}
        self.response = self.client.post(self.url, data, format='json')

    def test_question_creation_db(self):
        self.movie = Question(question_text="My entry title", pub_date='2018-12-24T13:45:25Z')
        self.movie.save()
        self.assertEqual(Question.objects.count(), 2)

    def test_question_creation_post(self):
        self.assertEqual(201, self.response.status_code)

    def test_get_created_question(self):
        getQuestion = self.client.get(self.url, format="json")
        # pdb.set_trace()
        self.assertEqual(getQuestion.data["count"], 1)

    def test_update_question(self):
        response_put = self.client.put('http://localhost:8000/api/polls/1/', {
            'question_text': 'Update',
            'pub_date': '2018-12-24T13:45:25Z',
            'pk': 1
        }, format="json")
        pdb.set_trace()
        self.assertEqual('Update', response_put.data['question_text'])


