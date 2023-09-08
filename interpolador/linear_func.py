# -*- coding: latin-1 -*-
"""
Con siguiente formula, podemos interpolar linealmente el punto de datos dado 

Interpolacion lineal: y(x) = y1 + (x - x1) * ({(y2 - y1) }/{ (x2 - x1)})


"""
data_123 = {
    'street_name':'AVDA CORRIENTES',
    'building':123,
    'coordinates':'-34.60270881835972, -58.36923688475535'
}

data_1585 = {
    'street_name':'AVDA CORRIENTES',
    'building':1585,
    'coordinates':'-34.604142,-58.389029'
}

data_1622 = {
    'street_name':'AVDA CORRIENTES',
    'building':1622,
    'coordinates':'-34.604385,-58.389808'
}

data_1642 = {
    'street_name':'AVDA CORRIENTES',
    'building':1642,
    'coordinates':'-34.604403,-58.390009'
}

data_1675 = {
    'street_name':'AVDA CORRIENTES',
    'building':1675,
    'coordinates':'-34.604265,-58.390371'
}

data_1780 = {
    'street_name':'AVDA CORRIENTES',
    'building':1780,
    'coordinates':'-34.604543,-58.391808'
}

data_1800 = {
    'street_name':'AVDA CORRIENTES',
    'building':1800,
    'coordinates':'-34.60453470157274, -58.39212651481816'
}

def linear_interpolation(x, y): 
    """_summary_

    Args:
        x (float): Datos del punto
        y (float): Punto a buscar

    Returns:
        _type_: _description_
    """     
    output = x[0][1] + (y - x[0][0]) * ((x[1][1] - x[0][1])/(x[1][0] - x[0][0]))
    return output
 
# Driver Code - 1 -
data_lat=[
    [1622, -34.604385],
    [1675, -34.604265]
    ]
 
lat_x=1642
 
# Finding the interpolation
lat = linear_interpolation(data_lat, lat_x)

data_lng=[
    [1622, -58.389808],
    [1675, -58.390371]
    ]
 
lng_x=1642
 
# Finding the interpolation
lng = linear_interpolation(data_lng, lng_x)


print(lat , lng)

# Driver Code - 2 -

def get_points(point_x, point_y):
    data_lat = [
        [point_x['building'], float(point_x['coordinates'].split(',')[0])],
        [point_y['building'], float(point_y['coordinates'].split(',')[0])]
    ]
    data_lng = [
        [point_x['building'], float(point_x['coordinates'].split(',')[1])],
        [point_y['building'], float(point_y['coordinates'].split(',')[1])]
    ]

    return data_lat, data_lng

print(get_points(data_1622, data_1675))

def get_interpolation_point(building, point_a, point_b):
    data_lat, data_lng = get_points(point_a, point_b)
    lat = linear_interpolation(data_lat, building)
    lng = linear_interpolation(data_lng, building)
    return lat, lng

print('Interpolacion punto 1642, data 123, 1800')
print(get_interpolation_point(1642, data_123, data_1800))
print('Interpolacion punto 1642, data 1585, 1675')
print(get_interpolation_point(1642, data_1585, data_1675))
print('Interpolacion punto 1642, data 1622, 1780')
print(get_interpolation_point(1642, data_1622, data_1780))