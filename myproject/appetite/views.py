from django.shortcuts import render
from django.http import HttpResponseBadRequest 

from .models import Shoe

def create_shoe(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if not type:
            # Handle the case where 'type' is not provided
            return HttpResponseBadRequest("Type is required.")

        brand = request.POST.get('brand')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        shoe = Shoe(type=type, brand=brand, description=description, price=price, image=image)
        shoe.save()

    return render(request, 'upload_media.html')



# shoes/views.py
from rest_framework import generics
from django.shortcuts import render
from .models import Shoe
from .serializers import ShoeSerializer

class ShoeListCreateView(generics.ListCreateAPIView):
    queryset = Shoe.objects.all().order_by('-id')  # Order by ID to get the latest first
    serializer_class = ShoeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Check if the request wants JSON or HTML
        if self.request.accepted_renderer.format == 'html':
            context = {'shoes': serializer.data}
            return render(request, 'shoes/list_shoes.html', context)
        else:
            return super().list(request, *args, **kwargs)

