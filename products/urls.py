from django.urls import path, include

from . import views

from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'product_category_set', views.ProductCategorySet)
# router.register(r'cat', views.CategorySet)
router.register(r'product_set', views.ProductSet)


app_name = 'products'


urlpatterns = [
    path('', include(router.urls)),
    path('cat/', views.CategorySet.as_view()),
    # path('categories/', views.ProductCategorySet.as_view(), name="categories"),
]
