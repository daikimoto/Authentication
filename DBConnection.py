import MySQLdb
import Constration as Const

# ユーザ認証情報テーブルからのユーザ情報取得
def getUserInfo(inputAuth):
    
    # DBに接続
    conn = MySQLdb.connect(host=Const.DB_HOST, user=Const.DB_USER, passwd=Const.DB_PASS, db=Const.DB)
    cur = conn.cursor()
    sql = 'select * from user_auth where user_id = "{}";'.format(inputAuth)
    
    try:
        cur.execute(sql)
        userInfo = cur.fetchone()
        return userInfo[0], userInfo[1]
    except TypeError:
        return None,None
    
def addUserInfo(user_id, user_password):
    
    if(isExistedInputAuthID(user_id)):
        print("ユーザID : '{}'はすでに使用されています。".format(user_id))
    else:
        conn = MySQLdb.connect(host=Const.DB_HOST, user=Const.DB_USER, passwd=Const.DB_PASS, db=Const.DB)
        cur = conn.cursor()
        sql = 'insert into {} values ("{}", "{}")'.format(Const.USER_AUTH_TABLE,user_id, user_password)
        cur.execute(sql)
        conn.commit()
        print("新規ユーザを追加しました。")

# 入力されたユーザIDがユーザ認証情報テーブルに存在するかチェック
def isExistedInputAuthID(inputAuthID):
    
    conn = MySQLdb.connect(host=Const.DB_HOST, user=Const.DB_USER, passwd=Const.DB_PASS, db=Const.DB)
    cur = conn.cursor()
    sql = 'select * from user_auth where user_id = "{}";'.format(inputAuthID)
    
    if(cur.execute(sql) == 0):
        return False
    else:
        return True