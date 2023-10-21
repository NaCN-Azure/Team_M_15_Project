# Packaged sql sentences dealing with User Tables
# TODO...
def startOrder(Order):
    # TODO
    return

def endOrder(id):
    # TODO
    return

def getOrder(id):
    return 'select * from "order" where id = {}'.format(id)

def getUserOrder(user_id):
    return 'select * from "order" where user_id = {}'.format(user_id)