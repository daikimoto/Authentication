import DBConnection as DBConn
import Constration as Const

def Authencation():
    
    auth_count = 0
    while auth_count < Const.MAX_AUTH:

        # 認証情報を入力させる
        print(Const.AUTH_START_MESSAGE)
        auth_id = input(Const.USER_ID_INPUT_MESSAGE)
        auth_password = input(Const.PASSWORD_INPUT_MESSAGE)

        # DBからユーザ情報取得
        user_id, user_password = DBConn.getUserInfo(auth_id)

        # 認証情報とユーザ情報のパスワード一致チェック
        if(isMatchedPassword(auth_password, user_password)):
            print(Const.AUTH_SUCCESS_MESSAGE)
            return True
        else:
            auth_count += 1
            print(str(auth_count) + Const.AUTH_FAULT_MESSAGE)

    return False
            
# 認証情報入力データチェック
def isCheckedInputAuthInfoData(input):
    return 0

# 認証情報とユーザ情報のパスワード一致チェック
def isMatchedPassword(auth_password, user_password):
    if(auth_password == user_password):
        return True
    else:
        return False
