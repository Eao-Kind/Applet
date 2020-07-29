import time
from wxpy import *
import random


class IamStrong:
    def __init__(self, groupName, sendMessage):
        self.bot = Bot(cache_path=True)  # 机器人登陆微信
        self.mssagelist = ["不谈", "假装睡觉？", "Wubba lubba dub dub", "OK", "ok休息",
                           "强者", "上当", "没人？", "折磨", "颠倒怪", "慢性自杀", "无敌", "起飞"]
        self.groupName = groupName
        self.wxpygroups = self.checkFindGroup(sendMessage=sendMessage)

    def checkFindGroup(self, sendMessage):
        '''
        :param bot:  微信机器人
        :param groupName: 需要发送信息的群聊名称
        :return: 找到的群聊
        '''

        Groups = self.bot.groups()
        print("微信群聊如下：")
        for i in Groups:
            print(i)
        try:
            wxpygroups = self.bot.groups().search(self.groupName)[0]  # 根据群名 搜索群聊
            wxpygroups.send(sendMessage)  # 找到后发一条自定义消息验证是否成功
        except:
            print("查找群失败")
        return wxpygroups

    def getRandomMessage(self):
        '''
        :return: 随机信息列表里面的随机一条信息
        '''
        randommssage = self.mssagelist[random.randint(0, len(self.mssagelist)-1)]  # 获取随机一个消息
        return randommssage

    def sendNews(self, sleepTime):
        '''
        :param groupName: 需要发送信息的群聊名称
        :return:
        '''
        self.bot.enable_puid()  #
        print("下次发送信息的时间为：" + time.asctime(time.localtime(time.time() + sleepTime)))
        time.sleep(sleepTime)  # 随机停止时间
        randommssage = self.getRandomMessage()  # 获取随机信息
        self.wxpygroups.send(randommssage)  # 发送消息
        print("发送消息成功：" + randommssage)


if __name__ == '__main__':
    #send_news()

    groupName = '臭🍐'
    mybot = IamStrong(groupName=groupName, sendMessage="")  # 初始化 我是强者 自动调用 checkFindGroup 函数
    mybot.wxpygroups.send("")
    for i in range(0, 20, 1):
        mybot.sendNews(sleepTime=1800 + random.randint(1200, 3600))  # 根据随机间隔停止时间 发送信息
    embed()  # 暂时不退出



def send_news():
    bot = Bot(cache_path=True)  # 缓存连接微信,会出现一个登陆微信的二维码
    bot.enable_puid()
    Groups = bot.groups()
    wxpygroups = checkFindGroup(bot=bot, Groups=Groups)

    for i in range(0, 20, 1):
        randomTime = 1800 + random.randint(100, 1200)  # 获取一个停止时间
        print("下次发送信息的时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() + randomTime))
        time.sleep(randomTime)  # 随机停止时间
        randommssage = getRandomMessage()  # 获取随机信息
        wxpygroups.send(randommssage)  # 发送消息
        print("发送消息成功：" + randommssage)
    embed()  # 暂时不退出


def getRandomMessage():
    mssagelist = ["不谈", "假装睡觉？", "Wubba lubba dub dub", "OK", "ok休息",
                  "强者", "上当", "没人？", "折磨", "颠倒怪", "慢性自杀", "无敌"]
    randommssage = mssagelist[random.randint(0, len(mssagelist))]  # 获取随机一个消息
    return randommssage


def checkFindGroup(bot, Groups):
    for i in Groups:
        print(i)
    try:
        wxpygroups = bot.groups().search('🍐哥的爬爬虫 ')[0]  # 根据群名 搜索群聊
        # wxpygroups.send("今晚我是最强者不谈")  # 找到后发一条消息验证是否成功
        print(wxpygroups.puid)
    except:
        print("查找群失败")

    for i in Groups:
        if i == '<Group: 🍐 🈹 [睡] 🤤>':
            print("找到群了")
            break
    return wxpygroups
