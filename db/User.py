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

def getAllOpertor():
    return 'select * from user where user_type = 2'

def updateUserInfo(user):
    return 'update user ' \
           'set user_name = {}, email = {}, phone = {}, birthday = {}, city = {}' \
           ''.format(user['user_name'],user['email'],user['phone'],user['birthday'],user['city'])

def login(email):
    return 'select id, password, salt, user_type from user where email = \'{}\''.format(email)

def register(username,email,phone,salt,password):
    data = """
    INSERT INTO user (user_name, email, phone, salt, password, wallet, city, user_type)
    VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', 0.0, 'Glasgow', 1)
    """.format(username,email,phone,salt,password)
    return data