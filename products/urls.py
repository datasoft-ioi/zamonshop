from django.urls import path, include

from . import views

from rest_framework import routers, serializers, viewsets

from django.urls import path
from .views import CategoryList, CategoryDetail



router = routers.DefaultRouter()
router.register(r'product_category_set', views.ProductCategorySet)
# router.register(r'cat', views.CategorySet)
router.register(r'product_set', views.ProductSet)


app_name = 'products'


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # path('categories/', views.ProductCategorySet.as_view(), name="categories"),
]
