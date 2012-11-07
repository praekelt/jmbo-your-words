from django import template
from jmboyourwords.models import YourStoryCompetition
from django.contrib.sites.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_your_words_competitions(context, limit=5, var_name='your_words_list'):
    stories = YourStoryCompetition.objects.filter(published=True)\
                                          .filter(sites=Site.objects.get_current())\
                                          .order_by('-publish_on')
    context[var_name] = stories
    return ""
