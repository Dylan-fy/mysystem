from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name="index"),
    url(r'^login/$', 'mainframe.views.login', name="login"),
    url(r'^register/$', 'mainframe.views.register', name="register"),
    url(r'^management_user/$', 'mainframe.views.management_user', name="management_user"),
    url(r'^management_computer/$', 'mainframe.views.management_computer', name="management_computer"),
    url(r'^account_setting/$', 'mainframe.views.account_setting', name="account_setting"),
)
