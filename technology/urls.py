from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from component_showcase import settings
from technology.api import TechnologyAPI

urlpatterns = [
    # url(r'^technology/(?P<pk>[0-9]+)/$', TechnologyAPI.as_view()),
    url(r'^technology/', TechnologyAPI.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
