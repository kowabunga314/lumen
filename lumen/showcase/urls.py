from django.urls import path
from showcase import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<series_name>', views.get_series, name='series_detail'),
]