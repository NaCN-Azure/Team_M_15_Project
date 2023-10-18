# Packaged sql sentences dealing with User Tables
# TODO...

def createReport(report):
    # TODO
    return

def getReportByOrderId(id):
    return 'select * from report where order_id = {}'.format(id)

def getReportByUserId(user_id):
    return 'select * from report where user_id = {}'.format(user_id)

def getReportByBikeId(bike_id):
    return 'select * from report where bike_id = {}'.format(bike_id)

def getAllReport():
    return 'select * from report'

def getReportByStatus(status):
    x= 0
    if status=='Done':
        x = 1
    elif status=='Unfinished':
        x = 0
    return 'select * from report where is_solved = {}'.format(x)

def doneReport(id):
    return 'update report set is_solved = 1 where id = {}'.format(id)