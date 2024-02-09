from django.shortcuts import render
from django.http import HttpResponseBadRequest 
from rest_framework import generics, renderers
from .models import Shoe
from .serializers import ShoeSerializer

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

class ShoeListCreateView(generics.ListCreateAPIView):
    queryset = Shoe.objects.all().order_by('-id')  # Order by ID to get the latest first
    serializer_class = ShoeSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer]  # Corrected class name

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        # Fetch search parameters from the request GET parameters
        shoe_type = self.request.GET.get('type')
        brand = self.request.GET.get('brand')

        # Apply filters based on search parameters
        if shoe_type:
            queryset = queryset.filter(type=shoe_type)
        if brand:
           queryset = queryset.filter(brand__iexact=brand)


        serializer = self.get_serializer(queryset, many=True)

        # Always render the HTML template
        context = {'shoes': serializer.data}
        return render(request, 'shoe_list.html', context)
