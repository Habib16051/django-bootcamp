from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Bangladesh Cricket Board</h>")
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "Habib!", "query": query}
    return render(request, "home.html", context)


def product_view_list(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, 'products/list.html', context)


def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    return render(request, "products/details.html", {"object": obj})


def product_api_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return JsonResponse({"id": obj.id})

# def bad_view(request, *args, **kwargs):
# print(dict(request.GET))
# my_request_data = dict(request.GET)
# new_product = my_request_data.get("new_product")
# print(my_request_data, new_product)
# if new_product[0].lower() == "true":
#   print(new_product)
#  Product.objects.create(title=my_request_data.get("title")[0], content=my_request_data.get("content")[0])
# return HttpResponse(" Don't come again! I don't wanna see you ever!")
#
