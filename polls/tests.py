from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Questions
from django.urls import reverse

# Create your tests here.

def cretae_question(question_text, days):
    time=timezone.now() + datetime.timedelta(days=days)
    return Questions.objects.create(question_text=question_text,pub_date=time)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        response=self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        question=cretae_question(question_text="hello",days=-30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],[question]
        )

    def test_future_question(self):
        question=cretae_question(question_text="future",days=30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],[]
        )

    def test_future_past_question(self):
        question=cretae_question(question_text="past",days=-30)
        cretae_question(question_text="future",days=30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question])

    def test_two_past_question(self):
        question1=cretae_question(question_text="past1",days=-30) 
        question2=cretae_question(question_text="past1",days=-30) 
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question2,question1])


class QuestionDetailViewTests(TestCase):
    def test_future_questions(self):
        question=cretae_question(question_text="future",days=30)
        response=self.client.get(reverse("polls:detail",args=(question.id,)))
        self.assertEqual(response.status_code,404)
    
    def test_past_question(self):
        past_question=cretae_question(question_text="past",days=-30)
        response=self.client.get(reverse("polls:detail",args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question=Questions(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question= Questions(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)
    
    def test_was_published_recently_with_recent_question(self):
        time= timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question=Questions(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)