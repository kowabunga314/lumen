from datetime import datetime, timezone
from django.test import TestCase
from django.urls import resolve, reverse
from showcase.models import Photo, Series
from showcase.views import index, get_series

# Create your tests here.
class SeriesModelTests(TestCase):
    
    def test_empty_series_has_zero_length(self):
        '''
            Tests that series with no photos returns 0 for length
        '''
        empty_series = Series(name='empty_series')
        self.assertIs(empty_series.photo_count(), 0)

    def test_series_length_of_one(self):
        '''
            Tests that series with a single photo returns 1 for length
        '''
        series = Series(name='series')
        series.save()
        p1 = Photo(name='p1', series=series)
        p1.save()
        self.assertIs(series.photo_count(), 1)


def create_series(name, description):
    time = timezone.now() + datetime.timedelta(days=1)
    return Series.objects.create(name=name, description=description, pub_date=time)

class ShowcaseIndexViewTests(TestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_detail_url_resolved(self):
        url = reverse('series_detail', args=['slug'])
        self.assertEqual(resolve(url).func, get_series)

