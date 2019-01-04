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
        self.pk = 1

        # create question db method
        self.movie = Question(question_text=self.name, pub_date=self.date)
        self.movie.save()
        self.assertEqual(Question.objects.count(), 1)

    def test_check_polls_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    # create question post method
    def test_create_question_post_method(self):
        data = {'question_text': self.name,
                'pub_date': self.date,
                '_content_type': "application/json"}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(201, response.status_code)

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
            'pk': self.pk
        }, format="json")

        # pdb.set_trace()
        self.assertEqual(self.new_name, response_put.data['question_text'])


