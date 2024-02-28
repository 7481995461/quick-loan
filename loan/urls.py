from django.urls import path
from .views import Vendor_List_Create,User_detail_update_delete
urlpatterns = [
    path('create_user/',Vendor_List_Create.as_view(),name="create-user"),
    path('user/<str:phone_number>/', User_detail_update_delete, name='User-detail-update-delete'),
]
