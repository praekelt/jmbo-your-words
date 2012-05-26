from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('jmboyourwords.views',
    url(r'^(?P<competition_id>\d+)/$',\
        'your_story',\
        name='your_story'),
)
