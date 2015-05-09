from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'evoluirmais.core.views.home', name='home'),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
