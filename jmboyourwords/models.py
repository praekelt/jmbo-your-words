from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from jmboyourwords.managers import PublishedManager
from pml.utils import sanitize_html


class YourStoryCompetition(models.Model):
    published = models.BooleanField(default=False)
    publish_on = models.DateTimeField(blank=True, null=True)
    retract_on = models.DateTimeField(blank=True, null=True)

    # Content
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='your_words/', blank=True)
    content = models.TextField()
    terms_and_conditions = models.TextField(
        help_text="Please supply the terms and conditions text for this \
                   competition."
    )

    # Organisation
    categories = models.ManyToManyField('category.Category',\
                                        blank=True, null=True)
    tags = models.ManyToManyField('category.Tag', blank=True, null=True)

    # Meta
    author = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    sites = models.ManyToManyField(Site)

    objects = models.Manager()
    published_objects = PublishedManager()

    def save(self, *args, **kwargs):
        self.content = sanitize_html(self.content)
        super(YourStoryCompetition, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-publish_on',)
        get_latest_by = ('publish_on',)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('your_words_detail', None, {
            'pk': self.pk
        })


class YourStoryEntry(models.Model):
    """Story submissions by users"""
    your_story_competition = models.ForeignKey('YourStoryCompetition')
    user = models.ForeignKey(User, related_name='your_words_entires')
    name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=True)
    text = models.TextField(blank=False)
    terms = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Your story entry'
        verbose_name_plural = 'Your story entries'
        ordering = ('-created',)
        get_latest_by = ('created',)

    def __unicode__(self):
        return u"Story by %s" % self.name
