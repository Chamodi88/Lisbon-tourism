from django.contrib.gis.geos import Point
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, render_to_response
from django.utils.safestring import mark_safe
from django.utils.html import escapejs
from .forms import AttractionForm, QueryForm
from .models import Attraction
from django.views import generic
from django.contrib.gis.db.models.functions import Distance
import json

# Creating the views.

def all_appgps(request):
    """
    Obtaing parameter to limit number of travel locations
    """
    appgps = Attraction.objects.all()
    form = QueryForm(request.GET or None)
    a = request.GET.get('keynumbers')
    if a is None:
        x = 94
    else:
        x = int(a)

    b = request.GET.get('lat')
    if b is None:
        latitude = 38
    else:
        latitude = float(b)
   
    c = request.GET.get('lon')
    if c is None:
        longitude = -9
    else:
        longitude = float(c) 
    
    # Determining nearby locations.
    
    user_location = Point(longitude, latitude, srid=4326)
    appgps = Attraction.objects.annotate(distance=Distance('Geometry', user_location)
    ).order_by('distance')[0:x]
    
    map_appgps = [{'loc':[float(attraction.Latitude), float(attraction.Longitude)], 
                  'Name':attraction.Name,} for attraction in appgps]
    context = {
        'appgps':appgps,
        'map_appgps': mark_safe(escapejs(json.dumps(map_appgps))),
        'form':form}
    return render(request, 'appgps/appgps.html', context)

# Uploading details of new attractions to the database.
def addnew_attraction(request):
    form = AttractionForm(None)
    if request.method == "POST":
        form = AttractionForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Latitude = form.cleaned_data['Latitude']
            Latitude = float(str.format('{0:.6f}', float(Latitude)))
            Longitude = form.cleaned_data['Longitude']
            Longitude = float(str.format('{0:.6f}', float(Longitude)))
            Address = form.cleaned_data['Address']
            Opening_hours = form.cleaned_data['Opening_hours']
            Website = form.cleaned_data['Website']
            Tickets = form.cleaned_data['Tickets']
            attraction = Attraction(
                Name=Name, 
                Latitude=Latitude, 
                Longitude=Longitude, 
                Address=Address,
                Opening_hours=Opening_hours,
                Website=Website,
                Tickets=Tickets,
                Geometry=Point(Longitude, Latitude, srid=4326))
            attraction.save()
            return redirect('appgps:all')
    return render(request, 'appgps/addnew.html', {'form':form})

