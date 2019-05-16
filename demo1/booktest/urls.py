from django.conf.urls import url
from . import views

app_name='booktest'
urlpatterns=[
    url('^index/$',views.index,name='index'),
    url('^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^delebook/(\d+)/$',views.delebook,name='delebook'),
    url(r'^delehero/(\d+)/$',views.delehero,name='delehero'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^updatebook/(\d+)/$',views.updatebook,name='updatebook'),
    url(r'^updatehero/(\d+)/$',views.updatehero,name='updatehero')

]

# urlpatterns=[
#     url('^index/$',views.index),
#     url('^list/$',views.list),
#     url(r'^detail/(\d+)/$',views.detail)
#
# ]