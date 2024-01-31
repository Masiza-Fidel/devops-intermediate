# shoes/urls.py
from django.urls import path
from .views import create_shoe
from .views import ShoeListCreateView


urlpatterns = [
    path('', create_shoe, name='create_shoe'),
    path('shoes/', ShoeListCreateView.as_view(), name='shoe-list-create'),

    # Add other URL patterns as needed
]
