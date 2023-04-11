from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, CategoryDetail, SubcategoryViewSet, SubcategoryDetail, ProductList, ProductDetail

app_name = "products"

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)



urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('cat/', include(router.urls)),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # path('subcategdories/', SubcategoryViewSet, name='subcategory-list'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]