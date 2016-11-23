from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'Raffle_App.views.home', name='home'),
    url(r'^winner/','Raffle_App.views.winner' ,name = 'winner' ),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
