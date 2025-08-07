# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Simplify by including the router under 'restaurant/'
    path('restaurant/', include(router.urls)),  # This includes the BookingViewSet routes
    
    # Include other routes (e.g., for menu) inside restaurant.urls
    path('restaurant/', include('restaurant.urls')),  # Include the rest of restaurant's URLs
]
