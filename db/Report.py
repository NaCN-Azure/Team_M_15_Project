# Packaged sql sentences dealing with User Tables
# TODO...

def createReport(user_id,order_id,bike_id,message,problem_type,date):
    data = """
    INSERT INTO report (user_id, order_id, bike_id, message, problem_type, is_solved, city, date)
    VALUES ({}, {}, {}, \'{}\', \'{}\', 0, 'Glasgow', \'{}\')
    """.format(user_id,order_id,bike_id,message,problem_type,date)
    return data

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

def getReportByStatusAndUserId(status,user_id):
    x= 0
    if status=='Done':
        x = 1
    elif status=='Unfinished':
        x = 0
    return 'select * from report where is_solved = {} and user_id = {}'.format(x,user_id)

def doneReport(id):
    return 'update report set is_solved = 1 where id = {}'.format(id)