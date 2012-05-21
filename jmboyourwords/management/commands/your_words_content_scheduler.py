from django.core.management.base import BaseCommand
from jmboyourwords.models import YourStoryCompetition
from datetime import datetime


class Command(BaseCommand):
    help = '(Un)Publish content based on the publish_on and retract_on fields'

    def handle(self, **options):
        self.publish()
        self.retract()

    def publish(self):
        YourStoryCompetition.objects.filter(publish_on__lt=datetime.now()) \
                        .filter(published=False) \
                        .update(published=True)

    def retract(self):
        YourStoryCompetition.objects.filter(retract_on__lt=datetime.now()) \
                        .filter(published=True) \
                        .update(published=False)
