from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from jmboyourwords.models import YourStoryCompetition, YourStoryEntry
from jmboyourwords.management.commands.your_words_content_scheduler\
    import Command
from datetime import date, timedelta, datetime


class YourStoryCompetitionTestCase(TestCase):
    fixtures = [
        'jmboyourwords/fixtures/test/yourwords/sample.json',
        'jmboyourwords/fixtures/test/auth/sample.json',
    ]

    def setUp(self):
        self.client = Client()
        self.client.login(username='27123456789', password='1234')

        yesterday = date.today() - timedelta(days=1)
        YourStoryCompetition.objects.all().update(publish_on=yesterday,\
                                                  retract_on=datetime.now())

    def test_competition_publishing(self):
        c = Command()

        self.assertFalse(YourStoryCompetition.objects.latest().published)

        c.publish()
        self.assertTrue(YourStoryCompetition.objects.latest().published)

        c.retract()
        self.assertFalse(YourStoryCompetition.objects.latest().published)

    def test_competition_entry(self):
        competition = YourStoryCompetition.objects.latest()
        resp = self.client.get(reverse('your_story', args=[competition.pk]))
        self.assertEquals(resp.status_code, 200)

        post_data = {
            'name': 'Test User',
            'email': 'testuser@email.com',
            'text': 'This is a sample entry story',
            'terms': 'True',
        }

        resp = self.client.post(reverse('your_story', args=[competition.pk]),\
                                post_data)
        self.assertEquals(resp.status_code, 302)

        latest_entry = YourStoryEntry.objects.latest()
        self.assertEquals(latest_entry.name, 'Test User')
        self.assertEquals(latest_entry.text, 'This is a sample entry story')

        post_data = {
            'name': 'Test User',
            'email': 'testuser@email.com',
            'text': 'This is another sample entry story',
            'terms': 'False',
        }

        resp = self.client.post(reverse('your_story', args=[competition.pk]),\
                                post_data)
        self.assertContains(resp, 'You must agree to the terms and conditions')
