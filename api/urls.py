from django.conf.urls import patterns, url
from api.views import *

urlpatterns = patterns('',

    url(r'^shopping/16/$', all_users, name='14'),
    url(r'^shopping/17/$', sellers_enabled, name='17'),
    url(r'^shopping/18/$', products_outOfStock, name='18'),
    url(r'^shopping/19/$', products, name='19'),
    url(r'^shopping/20/$', top5_products, name='20'),
    url(r'^shopping/21/$', unpublish_outofStock_products, name='21'),
    url(r'^shopping/22/$', products2, name='22'),
    url(r'^shopping/23/$', products3, name='23'),
    url(r'^shopping/24/$', products4, name='24'),
    url(r'^shopping/25/$', products5, name='25'),

    url(r'^user/list/$', list_users, name='list-user'),
    url(r'^user/add/$', add_user, name='add-user'),

    url(r'^seller/add/$', add_seller, name='add-seller'),

    url(r'^product/add/$', add_product, name='add-product'),

)

