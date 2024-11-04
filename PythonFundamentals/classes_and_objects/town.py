class Town:
    latitude = '0°N'
    longitude = '0°E'

    def __init__(self, name):
        self.name = name

    def set_latitude(self, new_latitude):
        Town.latitude = new_latitude

    def set_longitude(self, new_longitude):
        Town.longitude = new_longitude

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {Town.latitude} | Longitude: {Town.longitude}'

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)