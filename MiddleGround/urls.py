from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MiddleGround.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mground/', include('mground.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
