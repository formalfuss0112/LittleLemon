from rest_framework import generics
from .models import MenuItem  # Use MenuItem here
from .serializers import MenuItemSerializer  # Ensure this is imported
from rest_framework.permissions import IsAuthenticated

# List and Create MenuItems
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()  # Correct queryset
    serializer_class = MenuItemSerializer  # Use MenuItemSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete MenuItems
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()  # Correct queryset
    serializer_class = MenuItemSerializer  # Use MenuItemSerializer
    permission_classes = [IsAuthenticated]


from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
