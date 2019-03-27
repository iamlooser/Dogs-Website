from django.contrib import admin
from django.conf.urls import url, include
from dogs_website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', views.index, name="home"),
    url(r'^search/$', views.search),
    url(r'^sign-in/$', views.sign_in, name="signIn"),
    url(r'^signed-in/$', views.signed_in, name="signedIn"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^event/', include('event.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
