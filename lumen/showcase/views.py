from django.db.models import query
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from showcase.models import Photo, Series
from showcase.serializers import PhotoSerializer, SeriesSerializer
from rest_framework import permissions, viewsets


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a group of Series objects to be retrieved
    """
    queryset = Series.objects.all().order_by('name')
    serializer_class = SeriesSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a group of Photo objects to be retrieved
    """
    queryset = Photo.objects.all().order_by('-pub_date')
    serializer_class = PhotoSerializer


# Create your views here.
def index(request):
    # Get up to 5 different series
    series_list = Series.objects.order_by('name')[:5]

    # Make sure the series list has data
    if len(series_list) <= 0:
        raise Http404('No Series were found.')

    # Generate context
    context = {
        'series_list': series_list
    }
    
    # Render showcase page
    return render(request, 'showcase/index.html', context)


def get_series(request, series_name):
    # Look up requested series
    series = get_object_or_404(Series, name=series_name)

    # Generate context
    context = {'series': series}

    # Render series detail
    return render(request, 'showcase/series_detail.html', context)


