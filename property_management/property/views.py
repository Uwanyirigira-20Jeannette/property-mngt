
from django.http import HttpResponse
from django.shortcuts import render
from .models import Property
from django.shortcuts import render, get_object_or_404

def home(request):
    return HttpResponse("Welcome to Property Management!")



def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property/property_list.html', {'properties': properties})



def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property/property_detail.html', {'property': property})


