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
	url(r'^post/(?P<slug>[\w_-]+)/$', 'ecosite.blog.views.post_show', name='post-show'),
	url(r'^comentarios/', include('django.contrib.comments.urls')),
	url(r'^contato/', 'ecosite.contact.views.contact', name='contact'),
	url(r'^categoria/(?P<category_id>\d+)/$', 'ecosite.blog.views.show_posts_by_category', name='posts-by-category'),
)
