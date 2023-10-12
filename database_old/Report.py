# Packaged sql sentences dealing with User Tables
# TODO...

def createReport(report):
    # TODO
    return

def getReportByReportId(id):
    return 'select * from report where id = {}'.format(id)

def getReportByUserId(user_id):
    return 'select * from report where user_id = {}'.format(user_id)

def getReportByBikeId(bike_id):
    return 'select * from report where bike_id = {}'.format(bike_id)