import pyweather

api = pyweather.Api(
    auth_key='fd64b46cb9ac672d1f89c1a82f9122e7', lat='53.4', lon='-2.15')
print(api.get_temp())
