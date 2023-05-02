from django.urls import path
from .views import AdvertisementList, AdvertisementDetail, AdvertisementListByUsername

app_name = 'advertisement'

urlpatterns = [
    path('', AdvertisementList.as_view(), name='advertisement_list_create'),
    path('<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_retrieve_update_destroy'),
    path('<str:username>/', AdvertisementListByUsername.as_view(), name='advertisement_list_by_username'),
]