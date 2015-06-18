from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'livedoornews_reader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news.views.index'),
    url(r'^article/(?P<article_id>\d+)/$', 'news.views.article'),
    
)

urlpatterns += staticfiles_urlpatterns()