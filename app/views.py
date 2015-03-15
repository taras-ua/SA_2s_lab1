from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
import app.controllers.main as controller
from app.controllers.method import listOfTanksGeneric, listOfBMPGeneric, listOfPlanesGeneric, listOfShipsGeneric, listOfPVOGeneric, \
    listOfAircraftsGeneric, listOfFreightersGeneric


class GraphForm(forms.Form):
    tank_speed = forms.IntegerField(min_value=1)
    tank_fuel = forms.IntegerField(min_value=1)
    tank_gauge = forms.IntegerField(min_value=1)
    bmp_speed = forms.IntegerField(min_value=1)
    bmp_soldiers = forms.IntegerField(min_value=1)
    bmp_armor = forms.IntegerField(min_value=1)
    plane_speed = forms.IntegerField(min_value=1)
    plane_attack_radius = forms.IntegerField(min_value=1)
    plane_gauge = forms.IntegerField(min_value=1)
    plane_altitude = forms.IntegerField(min_value=1)
    ship_speed = forms.IntegerField(min_value=1)
    ship_carrying = forms.IntegerField(min_value=1)
    ship_planes_count = forms.IntegerField(min_value=1)
    ship_soldiers = forms.IntegerField(min_value=1)
    pvo_attack_radius = forms.IntegerField(min_value=1)
    pvo_speed = forms.IntegerField(min_value=1)
    pvo_attack_height = forms.IntegerField(min_value=1)
    aircraft_displacement = forms.IntegerField(min_value=1)
    aircraft_soldiers = forms.IntegerField(min_value=1)
    aircraft_autonomy = forms.IntegerField(min_value=1)
    aircraft_aviation = forms.IntegerField(min_value=1)
    freighter_range = forms.IntegerField(min_value=1)
    freighter_altitude = forms.IntegerField(min_value=1)
    freighter_carrying = forms.IntegerField(min_value=1)
    budget = forms.IntegerField(min_value=1)


def home(request):
    if request.method == 'GET':
        form = GraphForm(
            initial={
                'tank_speed': 50,
                'tank_fuel': 400,
                'tank_gauge': 105,
                'bmp_speed': 60,
                'bmp_soldiers': 7,
                'bmp_armor': 30,
                'plane_speed': 1900,
                'plane_attack_radius': 800,
                'plane_gauge': 20,
                'plane_altitude': 15,
                'ship_speed': 15,
                'ship_carrying': 20000,
                'ship_planes_count': 10,
                'ship_soldiers': 800,
                'pvo_attack_radius': 5,
                'pvo_speed': 1000,
                'pvo_attack_height': 10,
                'aircraft_displacement': 30000,
                'aircraft_soldiers': 1000,
                'aircraft_autonomy': 45,
                'aircraft_aviation': 20,
                'freighter_range': 4000,
                'freighter_altitude': 10000,
                'freighter_carrying': 100,
                'budget': 4000000000,
            }
        )
        return render_to_response('home.html',
                                  {
                                      'form': form,
                                      'tanks': listOfTanksGeneric,
                                      'apcs': listOfBMPGeneric,
                                      'planes': listOfPlanesGeneric,
                                      'ships': listOfShipsGeneric,
                                      'caws': listOfPVOGeneric,
                                      'aircrafts': listOfAircraftsGeneric,
                                      'freighters': listOfFreightersGeneric
                                  },
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            return redirect(controller.build_request(form))
        else:
            return HttpResponse(status=500)


def result(request):
    result = controller.main(request)
    return render_to_response('result.html', {'results': result}, context_instance=RequestContext(request))