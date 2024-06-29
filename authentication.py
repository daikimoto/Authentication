import MySQLdb
import Constration as Const

def Authencation():
    
    auth_count = 0
    while auth_count < Const.MAX_AUTH:

        # 認証情報を入力させる
        print(Const.AUTH_START_MESSAGE)
        auth_id = input(Const.USER_ID_INPUT_MESSAGE)
        auth_password = input(Const.PASSWORD_INPUT_MESSAGE)

        # DBからユーザ情報取得
        user_id, user_password = InputUserInfo(auth_id)

        # 認証情報とユーザ情報のパスワード一致チェック
        if(PassWordCheck(auth_password, user_password)):
            print(Const.AUTH_SUCCESS_MESSAGE)
            return True
        else:
            auth_count += 1
            print(str(auth_count) + Const.AUTH_FAULT_MESSAGE)

    return False
            



# DBからのユーザ情報取得
def InputUserInfo(inputAuth):
    
    # DBに接続
    conn = MySQLdb.connect(host=Const.DB_HOST, user=Const.DB_USER, passwd=Const.DB_PASS, db=Const.DB)
    cur = conn.cursor()

    sql = 'select * from user_auth where user_id = "{}";'.format(inputAuth)
    cur.execute(sql)
    userInfo = cur.fetchone()
    return userInfo[0], userInfo[1]

# 認証情報入力データチェック
def InputAuthInfoCheck(input):
    return 0

# 認証情報とユーザ情報のパスワード一致チェック
def PassWordCheck(auth_password, user_password):
    if(auth_password == user_password):
        return True
    else:
        return False
