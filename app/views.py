from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
import app.controllers.main as controller


class GraphForm(forms.Form):
    tank_speed = forms.IntegerField(min_value=1)
    tank_fuel = forms.IntegerField(min_value=1)
    tank_gauge = forms.IntegerField(min_value=1)


def home(request):
    if request.method == 'GET':
        form = GraphForm(initial={'tank_speed': 60, 'tank_fuel': 500, 'tank_gauge': 125})
        return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            return redirect(controller.build_request(form))
        else:
            return HttpResponse(status=500)


def result(request):
    return HttpResponse(status=200)