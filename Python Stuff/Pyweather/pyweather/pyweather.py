from get_info import GetInfo


class Api(object):
    kwargs = {'lat': None, 'lon': None}

    """

    API class takes arguments for country, city or zip code.
    the auth argument in the init is the user api key.

    """

    def __init__(self, auth_key=None, **location):
        self.auth = auth_key
        self.location = location
        self.location_info = {}
        get_info = GetInfo()
        # iterates over the kwargs and checks wether to use there current location or not
        for key, value in location.items():
            if value is not None and value != 'current':
                self.location_info[key] = value
            elif value == 'current':
                self.location_info[key] = (get_info.get_location()[key])

        self.info = get_info.get_weather(
            self.auth, self.location_info, 'metric')

        """ collects the dictionary which conatians all
        the weather info from get_info.py file """

    # splits the dictionary by info such as temp, condition, humidity

    def get_temp(self):
        return self.info['main']['temp']

    def get_temp_min(self):
        return self.info['main']['temp_min']

    def get_temp_max(self):
        return self.info['main']['temp_min']

    def get_pressure(self):
        return self.info['main']['pressure']

    def get_humidity(self):
        return self.info['main']['humidity']

    def get_condition(self):
        return self.info['weather']['main']

    def get_condition_description(self):
        return self.info['weather']['description']

    def get_condition_icon(self):
        return self.info['weather']['icon']

    def get_wind_speed(self):
        return self.info['wind']['speed']

    def get_wind_direction(self):
        return self.info['wind']['deg']
