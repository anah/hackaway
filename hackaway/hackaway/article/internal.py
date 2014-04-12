# -*- coding: utf-8 -*-

import requests
import json

import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def search(request, topic):

  payload = {
    'streamId': 'topic/' + topic,
    'hours': 8
  }

  url = 'http://cloud.feedly.com/v3/mixes/contents'

  logger.debug(url)

  data = requests.get(url, params=payload)

  if data.status_code == 200:
    response = HttpResponse(data.text)
    # response['Content-type'] = 'application/json'
    return response
  else:
    console.warning('ErrorCode from feedly: ' + data.status_code)
    response = HttpResponse(json.dumps({'items': ['No articles found']}))
    # response['Content-type'] = 'application/json'
    return response
    