from django.conf.urls import patterns, url

from .views import OmniArticlesView

urlpatterns = patterns(
    '',
    url(r'^omni/$',
        OmniArticlesView.as_view(),
        name="omni_articles"),
)
