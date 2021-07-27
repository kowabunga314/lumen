from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from showcase.models import Series

# Create your views here.
def index(request):
    series_list = Series.objects.order_by('name')[:5]
    template = loader.get_template('showcase/index.html')
    context = {
        'series_list': series_list
    }
    return HttpResponse(template.render(context, request))
