

def build_request(form):
    request = '/result/?'
    request += 'tank_speed={}'.format(form.cleaned_data['tank_speed'])
    request += '&tank_fuel={}'.format(form.cleaned_data['tank_fuel'])
    request += '&tank_gauge={}'.format(form.cleaned_data['tank_gauge'])
    return request