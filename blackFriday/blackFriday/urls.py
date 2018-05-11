from django.conf.urls import url, include
from django.contrib import admin
from blackFriday import settings

urlpatterns =[
    # Examples:
    # url(r'^$', 'blackFriday.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^shopping_route/shopping/', include('shopping.urls')),
    url(r'^shopping_route/recommendation/', include('recommendation.urls')),
]
