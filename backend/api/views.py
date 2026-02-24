import json
from django.http import JsonResponse
from products.models import Product
# Create your views here

def api_home(request, *args, **kwargs):
    model_data = Product.object.all().order-by("?").first()
    # print(request.GET)
    # print(request.POST)
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse({'message': 'Hi there , this is your Django API response!!'})
    return JsonResponse(data)
