from django.conf.urls import patterns, include, url
from lszy_site import settings

urlpatterns = patterns('',

    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),


    url(r'/company_1', 'webpage.views.company_1'),
    url(r'/company_2', 'webpage.views.company_2'),
    url(r'/company_3', 'webpage.views.company_3'),


    url(r'/product_1', 'webpage.views.product_1'),
    url(r'/product_2', 'webpage.views.product_2'),
    url(r'/product_3', 'webpage.views.product_3'),


    url(r'/article_1', 'webpage.views.article_1'),
    url(r'/article_2', 'webpage.views.article_2'),
    url(r'/article_3', 'webpage.views.article_3'),
    
    url(r'^$', 'webpage.views.index'),
) 
