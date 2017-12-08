from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^messages/", include("postman.urls", namespace="postman")),
    url(r'^$', TemplateView.as_view(template_name="site_base.html"), name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    