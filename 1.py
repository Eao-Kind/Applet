import http.cookiejar as cookielib
import requests
import re
import pymysql
from DBUtils.PooledDB import PooledDB
import time


def cookies(web_name):
    with open(web_name, 'r') as f:
        lnum, data = 0, '#LWP-Cookies-2.0\n'  # 从饼干获取到的格式头不对，此处进行替换
        temp = f.readlines()  # 由于只能使用一次读行，所有要设计一个变量保存读到的内容， 列表
        if temp[0] == "// Semicolon separated Cookie File\n":  # 判断是否未处理的文本:
            for line in temp[4:]:
                # print(line)
                data += line
            temp = re.sub('expires="(.*?)"', 'expires="2038-01-19 03:14:07Z"', data)  # 替换expires内容

            f.close()
            with open(web_name, 'w') as f:
                f.write(temp)
                f.close()
                print("{}cookie已处理".format(web_name))


def sign_in(web_name):
    bt_Session = requests.session()  # 创建一个会话
    try:
        bt_Session.cookies = cookielib.LWPCookieJar(filename=web_name + '.txt')
        bt_Session.cookies.load()  # 加载cookie
        return bt_Session
    except:
        print("{}的cookies加载失败".format(web_name))
        return None


def main(web_name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    session = sign_in(web_name)
    count = 0
    for i in range(36924, 60000, 1):
        urlid = "userdetails.php?id=" + (str)(i)
        try:
            s = session.get(urlid, headers=headers)
            time.sleep(10)  # 停止5秒
            rs = findRS(s.text)
            if (rs[1] != None):
                writeMysql(i, rs)
            else:
                count += 1
                print("null数量:" + str(count))
                #writeMysql(i, 'Null')
        except:
            print("--------------------")


def findRS(text):
    listtemp = []
    pattern = re.compile('.*?用户详情 - (.*?) 比特校园PT小乐园 - Powered by NexusPHP</title>'
                         + '.*?加入日期.*?<span title.*?>(.*?)前</span>', re.S)
    result = re.findall(pattern, text)
    rs0 = [i[0] for i in result]
    rs1 = [i[1] for i in result]
    listtemp.append(rs0[0])
    listtemp.append(rs1[0])
    return listtemp



def writeMysql(id, rs):
    try:
        print(id, rs[0], rs[1])
        cursor = conn.cursor()
        sql = "INSERT INTO userinfo(ID,username,t) VALUES(%s,%s, %s)"
        cursor.execute(sql, (id, rs[0], rs[1]))
        cursor.close()
    except:
        print("数据库操作失败")


# 线程池
pool = PooledDB(pymysql, 5, host='192.168.1.204', user='root', passwd='root', db='test', port=3306, setsession=[
    'SET AUTOCOMMIT = 1'])
conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了



if __name__ == '__main__':
    main("btschool")

