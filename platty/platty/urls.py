from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'platty.views.home', name='home'),
                       url(r'^create', 'platty.views.create', name='create'),
                       url(r'^find', 'platty.views.find', name='find'),
                       url(r'^parties/(\d+)', 'platty.views.party', name='party'),
                       url(r'^parties', 'platty.views.parties', name='parties'),
                       url(r'^login', 'platty.views.login', name='login'),
                       url(r'^profile', 'platty.views.profile', name='profile'),
                       url(r'^populate', 'platty.views.populate', name='populate'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^/', include('platty.urls')),
                       )
