# inventory/urls.py
from django.urls import path
from .views import CategoryView ,user_list,user_detail, SubCategoryView, InventoryView, AddCartView, DressDetailView, SpecView,BikeView, student_api, GetAllUsersView, ListCreateAPIView
from inventory import views
from .models import User
from .serializer import UserSerializer

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('subcategory/',SubCategoryView.as_view(),name='subcategory'),
    path('inventory/',InventoryView.as_view(),name='inventory'),
    path('addcart/',AddCartView.as_view(),name='addcart'),
    path('dress/',DressDetailView.as_view(),name='dress'),
    path('spec/',SpecView.as_view(),name='bike_spec'),
    path('bike/',BikeView.as_view(),name='bike'),
    path('std/',student_api, name="std"),
    path('user/',GetAllUsersView.as_view(),name='user'),
    path('users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),
    path('Userss/', user_list, name='user-list'),
    path('use/', user_detail, name='user-detail')
,
    

]    