# -*- coding: utf-8 -*-

import requests
import json

import logging

import os
from django.http import HttpResponse

logger = logging.getLogger('django.request')

def search(request, topic):

  payload = {
    'streamId': 'topic/' + topic,
    'hours': 8
  }

  url = 'http://cloud.feedly.com/v3/mixes/contents'

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
    

YANDEX_HOST = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate(request, target_language, tag):
  payload = {
    'key': os.environ['YANDEX_API_KEY'],
    'lang': target_language,
    'text': tag
  }
  res = requests.get(YANDEX_HOST, params=payload)
  data = json.loads(res.text, 'utf-8')

  if data['code'] == 200:
    return HttpResponse(json.dumps({ 'lang': data['lang'], 'translation': data['text']}))
  else:
    logger.warn('translation failed: ' + data)
    return HttpResponse(json.dumps({ 'lang': 'sv', 'translation': tag}))