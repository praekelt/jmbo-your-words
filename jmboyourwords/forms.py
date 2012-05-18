from django.forms import ModelForm
from jmboyourwords.models import YourStoryEntry


class YourStoryEntryForm(ModelForm):
    class Meta:
        model = YourStoryEntry
