from django.urls import path
from .views import ProductView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', ProductView)



urlpatterns = [
 
    ]

urlpatterns += router.urls
