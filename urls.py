from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from ecosite.blog.feeds import LatestPosts
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ecosite/', include('ecosite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/js'}),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',{'feed_dict': {'ultimos': LatestPosts}}),
	url(r'^$', 'ecosite.blog.views.post_index', name='post-index'),
)
