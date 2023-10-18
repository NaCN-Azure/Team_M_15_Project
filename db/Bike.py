# Packaged sql sentences dealing with User Tables
# TODO...

def createBike(Bike):
    # TODO
    return
def getBikeById(bike_id):
    return 'select * from bike where id = {}'.format(bike_id)
def getUserByBikeId(bike_id):
    return 'select is_use from bike where id = {}'.format(bike_id)
def updateLocation(id,longitude,latitude):
    return 'update bike set longtitue = {} and latitude = {} where id = {}'.format(longitude,latitude, id)
def getAllBike():
    return 'select * from bike'
def selectNearestBike(longitude,latitude,bike_type):
    # TODO
    return

def fix(id):
    return 'update bike set is_broken = 0 where id = {}'.format(id)

def changeBattery(id):
    return 'update bike set battery = 100 where id = {}'.format(id)

def getBikeByTypes(bike_type):
    return 'select * from bike where bike_type = \'{}\''.format(bike_type)
