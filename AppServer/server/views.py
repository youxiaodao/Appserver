# -*- coding: utf-8 -*-
import json
from django.conf.urls.defaults import *
from django.http import HttpResponse, Http404

def to_json(result):
    return json.dumps(result, ensure_ascii=False)

def init(request):
    if request.method != 'GET':
        raise Http404
    sn = request.REQUEST.get("deviceId", "")
    result = {'resultCode': '1000', 'resultMsg': 'success'}
    if not sn:
        result['resultCode'] = '1002'
        result['resultMsg'] = u'无sn参数'
        return HttpResponse(to_json(result))

    if sn:
        import hashlib
        md5 = hashlib.md5()
        md5.update(sn)
        token = md5.hexdigest()
        r_data = {
            'sn': sn,
            'token': token,
            'serverAddress': 'http://attsaas.f3322.net:9090',
        }

        result['resultData'] = r_data
        return HttpResponse(to_json(result))