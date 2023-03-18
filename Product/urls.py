from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('products/',Products,name='products'),
    path('saleproducts/',SaleProducts,name='saleproducts'),
    path('detailproduct/<int:id>/',ProductDetail,name='product'),
    #filters
    path('maleproducts/',GenMale,name='genmale'),
    path('femaleproducts/',GenFemale,name='genfemale'),
    path('speakers/',Speakers,name='speaker'),
    path('powerbanks/',PowerBanks,name='powerbank'),
    path('iwatch/',iwatch,name='iwatch'),
    path('headsts/',Headsets,name='headsets'),
    path('airpods/',Airpods,name='airpods'),
    path('chargers/',Chargers,name='chargers'),
    #ajax
    path('filter-data',filter_data,name='filter_data'),
]
