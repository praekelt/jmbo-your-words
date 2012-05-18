from django import template
from jmboyourwords.models import YourStoryCompetition

register = template.Library()


@register.simple_tag(takes_context=True)
def get_your_words_competitions(context, limit=5, var_name='your_words_list'):
    stories = YourStoryCompetition.objects.filter(published=True)\
                                          .order_by('-publish_on')
    context[var_name] = stories
    return ""
