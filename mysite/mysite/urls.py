from django.conf.urls import include, url
from django.contrib import admin


urlpattern = [
    url(r'^pools/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]