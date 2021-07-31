from django.test import TestCase
from showcase.models import Photo, Series

# Create your tests here.
class SeriesModelTests(TestCase):
    
    def test_empty_series_has_zero_length(self):
        empty_series = Series(name='empty_series')
        self.assertIs(empty_series.photo_count(), 0)
