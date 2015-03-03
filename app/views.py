from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
import app.controllers.main as controller
from app.controllers.method import listOfTanks


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
    budget = forms.IntegerField(min_value=1)


def home(request):
    if request.method == 'GET':
        form = GraphForm(
            initial={
                'tank_speed': 60,
                'tank_fuel': 500,
                'tank_gauge': 125,
                'bmp_speed': 60,
                'bmp_soldiers': 5,
                'bmp_armor': 20,
                'plane_speed': 300,
                'plane_attack_radius': 1,
                'plane_gauge': 50,
                'plane_altitude': 500,
                'ship_speed': 60,
                'ship_carrying': 10,
                'ship_planes_count': 1,
                'ship_soldiers': 100,
                'pvo_attack_radius': 5,
                'pvo_speed': 500,
                'pvo_attack_height': 5,
                'budget': 500000,
            }
        )
        return render_to_response('home.html',
                                  {
                                      'form': form,
                                      'tanks': listOfTanks
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
    return HttpResponse(status=200)