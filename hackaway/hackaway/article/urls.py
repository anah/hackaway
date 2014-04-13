from django.conf.urls import patterns, url

from .views import OmniArticlesView, PaginatedArticleListView

urlpatterns = patterns(
    '',
    url(r'^omni/$',
        OmniArticlesView.as_view(),
        name="omni_articles"),
    url(r'^page(?P<page>[0-9]+)/$',
        PaginatedArticleListView.as_view(),
        name="articles"),
    url(r'^$',
        PaginatedArticleListView.as_view(),
        name="articles"),
)
