from app.controllers.method import Tank, Plane, Ship, PVO, BMP


def build_request(form):
    request = '/result/?'
    request += 'tank_speed={}'.format(form.cleaned_data['tank_speed'])
    request += '&tank_fuel={}'.format(form.cleaned_data['tank_fuel'])
    request += '&tank_gauge={}'.format(form.cleaned_data['tank_gauge'])
    request += '&bmp_speed={}'.format(form.cleaned_data['bmp_speed'])
    request += '&bmp_soldiers={}'.format(form.cleaned_data['bmp_soldiers'])
    request += '&bmp_armor={}'.format(form.cleaned_data['bmp_armor'])
    request += '&plane_speed={}'.format(form.cleaned_data['plane_speed'])
    request += '&plane_attack_radius={}'.format(form.cleaned_data['plane_attack_radius'])
    request += '&plane_gauge={}'.format(form.cleaned_data['plane_gauge'])
    request += '&plane_altitude={}'.format(form.cleaned_data['plane_altitude'])
    request += '&ship_speed={}'.format(form.cleaned_data['ship_speed'])
    request += '&ship_carrying={}'.format(form.cleaned_data['ship_carrying'])
    request += '&ship_planes_count={}'.format(form.cleaned_data['ship_planes_count'])
    request += '&ship_soldiers={}'.format(form.cleaned_data['ship_soldiers'])
    request += '&pvo_attack_radius={}'.format(form.cleaned_data['pvo_attack_radius'])
    request += '&pvo_speed={}'.format(form.cleaned_data['pvo_speed'])
    request += '&pvo_attack_height={}'.format(form.cleaned_data['pvo_attack_height'])
    request += '&budget={}'.format(form.cleaned_data['budget'])
    return request


def main(request):
    budget = int(request.GET.get('budget'))
    required_tank = Tank('',
                int(request.GET.get('tank_speed')),
                int(request.GET.get('tank_fuel')),
                int(request.GET.get('tank_gauge')), 0)
    required_plane = Plane('',
                int(request.GET.get('plane_speed')),
                int(request.GET.get('plane_altitude')),
                int(request.GET.get('plane_attack_radius')),
                int(request.GET.get('plane_gauge')), 0)
    required_ship = Ship('',
                int(request.GET.get('ship_speed')),
                int(request.GET.get('ship_carrying')),
                int(request.GET.get('ship_planes_count')),
                int(request.GET.get('ship_soldiers')), 0)
    required_pvo = PVO('',
                int(request.GET.get('pvo_attack_radius')),
                int(request.GET.get('pvo_speed')),
                int(request.GET.get('pvo_attack_height')), 0)
    required_bmp = BMP('',
                int(request.GET.get('bmp_speed')),
                int(request.GET.get('bmp_soldiers')),
                int(request.GET.get('bmp_armor')), 0)


    dictOfWishes = {'wishTankMaxSpeed':required_tank.maxSpeed,
                    'wishTankPowerOfMarch': ,
                    'wishTankCaliber': ,
                    'wishPlaneMaxSpeed': ,
                    'wishPlaneFlightAltitude': ,
                    'wishPlaneAttackRadius': ,
                    'wishPlaneCalibre': ,
                    'wishShipMaxSpeed': ,
                    'wishShipCarrying': ,
                    'wishShipPlanesOnBoard': ,
                    'wishShipSoldiers': ,
                    'wishPVOAttackRadius': ,
                    'wishPVOWarheadSpeed': ,
                    'wishPVOAttackHeight': }
    result_dictionary = []

    return result_dictionary