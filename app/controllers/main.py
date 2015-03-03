from app.controllers.method import purposefulSearchMethod


def build_request(form):
    request = '/result/?'
    request += 'wishTankMaxSpeed={}'.format(form.cleaned_data['tank_speed'])
    request += '&wishTankPowerOfMarch={}'.format(form.cleaned_data['tank_fuel'])
    request += '&wishTankCaliber={}'.format(form.cleaned_data['tank_gauge'])
    request += '&wishBMPMaxSpeed={}'.format(form.cleaned_data['bmp_speed'])
    request += '&wishBMPSoldiers={}'.format(form.cleaned_data['bmp_soldiers'])
    request += '&wishBMPArmor={}'.format(form.cleaned_data['bmp_armor'])
    request += '&wishPlaneMaxSpeed={}'.format(form.cleaned_data['plane_speed'])
    request += '&wishPlaneAttackRadius={}'.format(form.cleaned_data['plane_attack_radius'])
    request += '&wishPlaneCalibre={}'.format(form.cleaned_data['plane_gauge'])
    request += '&wishPlaneFlightAltitude={}'.format(form.cleaned_data['plane_altitude'])
    request += '&wishShipMaxSpeed={}'.format(form.cleaned_data['ship_speed'])
    request += '&wishShipCarrying={}'.format(form.cleaned_data['ship_carrying'])
    request += '&wishShipPlanesOnBoard={}'.format(form.cleaned_data['ship_planes_count'])
    request += '&wishShipSoldiers={}'.format(form.cleaned_data['ship_soldiers'])
    request += '&wishPVOAttackRadius={}'.format(form.cleaned_data['pvo_attack_radius'])
    request += '&wishPVOWarheadSpeed={}'.format(form.cleaned_data['pvo_speed'])
    request += '&wishPVOAttackHeight={}'.format(form.cleaned_data['pvo_attack_height'])
    request += '&budget={}'.format(form.cleaned_data['budget'])
    return request


def main(request):

    request_dictionary = request.GET.dict()
    for key in request_dictionary:
        request_dictionary[key] = int(request_dictionary[key])
    result = purposefulSearchMethod(request_dictionary)

    return result