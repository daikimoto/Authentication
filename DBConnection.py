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
        return 0,0

# 入力されたユーザIDがユーザ認証情報テーブルに存在するかチェック
def isExistedInputAuthID(inputAuthID):
    return 0