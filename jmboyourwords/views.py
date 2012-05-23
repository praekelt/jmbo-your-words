from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from jmboyourwords.models import YourStoryCompetition
from jmboyourwords.forms import YourStoryEntryForm


@login_required
def your_story(request, competition_id):
    competition = get_object_or_404(YourStoryCompetition, pk=competition_id)
    redirect_to = request.POST.get('next', '/')

    if request.method == 'POST':
        form = YourStoryEntryForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.your_story_competition = competition
            instance.save()
            return redirect(redirect_to)
    else:
        form = YourStoryEntryForm()

    return direct_to_template(request, 'yourwords/your_story.html', {
        'competition': competition,
        'form': form
        })
