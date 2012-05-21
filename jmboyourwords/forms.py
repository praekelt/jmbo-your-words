from django.forms import ModelForm, ValidationError
from jmboyourwords.models import YourStoryEntry


class YourStoryEntryForm(ModelForm):
    class Meta:
        model = YourStoryEntry
        exclude = ('user', 'your_story_competition')

    def clean_terms(self):
        terms = self.cleaned_data['terms']

        if terms == False:
            raise ValidationError(u'You must agree to the terms and conditions')

        return terms
