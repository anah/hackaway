from django.views.generic import View

import logging
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin

from .models import Article

logger = logging.getLogger('django.request')


class OmniArticlesView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    http_method_names = ['post']
    require_json = True

    def post(self, request, *args, **kwargs):
        try:
            logger.info(self.request_json)
            omni_id = self.request_json[u'id']
            if Article.objects.filter(omni_id=omni_id).exists():
                return self.render_json_response({'status': 'OK'})
            article = Article()
            article.omni_id = self.request_json[u'id']
            article.author = self.request_json[u'author']
            article.category = self.request_json[u'category']
            article.title = self.request_json[u'title']
            article.text = self.request_json[u'text']
            article.title = self.request_json[u'title']
            image_urls = self.request_json[u'images']
            if image_urls:
                article.image_url = image_urls[0]
            article.save()
            article.add_tags(self.request_json[u'tags'])
        except KeyError, e:
            logger.debug(e)
            return self.render_json_response({'status': 'error'})
        return self.render_json_response({'status': 'OK'})
