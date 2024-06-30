import DBConnection as DBConn
import Constration as Const

def addUserData():

    print(Const.ADD_USER_INFO_EXPLAIN_MESSAGE)
    auth_id = input(Const.USER_ID_INPUT_MESSAGE)
    auth_password = input(Const.PASSWORD_INPUT_MESSAGE)
    DBConn.addUserInfo(auth_id, auth_password)