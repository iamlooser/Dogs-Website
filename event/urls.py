from django.conf.urls import url
from event import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.event, name="events"),
    url(r'^(?P<event_id>[0-9]+)/$', views.event_details),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
