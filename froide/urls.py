from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import ugettext as _

from django.contrib import admin
admin.autodiscover()

from django.contrib import databrowse
from publicbody.models import PublicBody, FoiLaw

databrowse.site.register(PublicBody)
databrowse.site.register(FoiLaw)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'froide.foirequest.views.index', name='index'),
    # Translators: request URL
    url(r'^%s/' % _('make-request'), include('froide.foirequest.make_request_urls')),
    # Translators: URL part
    url(r'^%s/' % _('requests'), include('froide.foirequest.urls')),
    # Translators: request URL
    url(r'^%s/' % _('request'), include('froide.foirequest.request_urls')),

    # Translators: URL part
    url(r'^%s/' % _('entity'), include('froide.publicbody.urls')),
    url(r'^%s/' % _('law'), include('froide.publicbody.law_urls')),

    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Translators: URL part
    (r'^%s/' % _('account'), include('account.urls')),
    # Translators: URL part
    (r'^%s/' % _('search'), include('haystack.urls')),
    # Translators: URL part
    (r'^%s/' % _('help'), include('froide.help_urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^databrowse/(.*)', user_passes_test(lambda u: u.is_superuser, login_url="/account/login/")(databrowse.site.root)),
)



if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
