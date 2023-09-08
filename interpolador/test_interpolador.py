import pytest
from geopy import distance
from interpolador.linear_func import get_points, get_interpolation_point


@pytest.mark.parametrize(
    "test_coordinates_result",
    [
        (-34.604248117916185, -58.390008631050236),
        (-34.60433971698113, -58.39002045283019),
        (-34.604382636465076, -58.39022019680448),
        (-34.6042199, -58.389878933333335),
        (-34.604405, -58.39006116455696)
    ]
)
@pytest.mark.parametrize('real_coordinates', [(-34.604248117916185, -58.390008631050236)])
def test_distance_interpolador(test_coordinates_result, real_coordinates):
    
    val = distance.distance(test_coordinates_result, real_coordinates).meters < 25

    assert True == val

@pytest.mark.parametrize(
    "point_x, point_y, expected",
    [
        (
            {
                'street_name':'AVDA CORRIENTES',
                'building':1622,
                'coordinates':'-34.604385,-58.389808'
            },
            {
                'street_name':'AVDA CORRIENTES',
                'building':1675,
                'coordinates':'-34.604265,-58.390371'
            },
            ([[1622, -34.604385], [1675, -34.604265]], [[1622, -58.389808], [1675, -58.390371]])
        )
    ]
)
def test_get_points(point_x, point_y, expected):
    resp_point = get_points(point_x, point_y)

    assert resp_point == expected

@pytest.mark.parametrize(
    "point_x, point_y, building",
    [
        (
            {
                'street_name':'AVDA CORRIENTES',
                'building':1585,
                'coordinates':'-34.604142,-58.389029'
            },
            {
                'street_name':'AVDA CORRIENTES',
                'building':1780,
                'coordinates':'-34.604543,-58.391808'
            },
            1639
        )
    ]
)
@pytest.mark.parametrize('real_coordinates', [(-34.604091064477046, -58.38990409232127)])
def test_get_interpolation_point_not_building_in_block(
    point_x, point_y, building, real_coordinates
    ):
    test_coord = get_interpolation_point(building, point_x, point_y)
    diff_meters = distance.distance(test_coord, real_coordinates).meters

    assert diff_meters <= 25


@pytest.mark.parametrize(
    "point_x, point_y, building",
    [
        (
            {
                'street_name':'AVDA CORRIENTES',
                'building':1622,    #1628
                'coordinates':'-34.604385,-58.389808'
            },
            {
                'street_name':'AVDA CORRIENTES',
                'building':1675,    #1671
                'coordinates':'-34.604265,-58.390371'
            },
            1639
        )
    ]
)
@pytest.mark.parametrize('real_coordinates', [(-34.604091064477046, -58.38990409232127)])
def test_get_interpolation_point_building_into_block(point_x, point_y, building, real_coordinates):
    test_coord = get_interpolation_point(building, point_x, point_y)
    diff_meters = distance.distance(test_coord, real_coordinates).meters

    assert diff_meters <= 30