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
    

YANDEX_TRANSLATE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
YANDEX_LANGUAGES = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

def translate(request, target_language, tag):
  payload = {
    'key': os.environ['YANDEX_API_KEY'],
    'lang': target_language,
    'text': tag,
    'locale': target_language
  }
  res = requests.get(YANDEX_TRANSLATE, params=payload)
  data = json.loads(res.text, 'utf-8')

  if data['code'] == 200:
    return HttpResponse(json.dumps({ 'lang': data['lang'], 'translation': data['text']}))
  else:
    logger.warn('translation failed: ' + data)
    return HttpResponse(json.dumps({ 'lang': 'sv', 'translation': tag}))

def languages(request):
  payload = {
    'key': os.environ['YANDEX_API_KEY'],
    'ui': 'en'
  }
  res = requests.get(YANDEX_LANGUAGES, params=payload)
  return HttpResponse(res.text)
