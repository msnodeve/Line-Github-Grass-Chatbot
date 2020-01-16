import pymysql


def getConnection():
    return pymysql.connect(host='127.0.0.1', user='root', password='1234', db='board', charset='utf8', port=23306)


def signUpUser(key, userId):
    conn = getConnection()
    cur = conn.cursor()
    result = cur.execute("INSERT INTO users(id, user_id) VALUES('" + key + "', '" + userId + "') ON DUPLICATE KEY UPDATE user_id = VALUES(user_id);")
    conn.commit()
    conn.close()
    return result


def getUsers():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users;")
    result = cur.fetchall()
    conn.close()
    return result


def getUser(key):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users where id = '" + key + "';")
    result = cur.fetchall()
    conn.close()
    return result