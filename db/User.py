# Packaged sql sentences dealing with User Tables
# TODO...

def getUserInfo(id):
    return 'select * from user where id = {} '.format(id)

def addMoney(id,money):
    return 'update user set wallet = wallet + {} where id = {}'.format(money,id)

def getSingleLabel(label,condition,value):
    return 'select {} from user where {} = \'{}\''.format(label,condition,value)

def getAllUser():
    return 'select * from user where user_type = 1'

def getAllManager():
    return 'select * from user where user_type = 3'

def updateUserInfo(user):
    return 'update user ' \
           'set user_name = {}, email = {}, phone = {}, birthday = {}, city = {}' \
           ''.format(user['user_name'],user['email'],user['phone'],user['birthday'],user['city'])

def login():
    # TODO
    return

def logout():
    # TODO
    return

def register():
    # TODO
    return