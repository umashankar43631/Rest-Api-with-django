from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def api_home(request, *args  ,**kwargs ):
    body = request.body
    data = {}
    try:
        data = json.dumps(body) # strin of JSON Data to Python Dictionary
    except:
        pass
    data['header'] = dict(request.headers)
    data['path'] = request.path
    data['content-type'] = request.content_type
    return JsonResponse(data)
