from wxpy import *
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from pandas import read_excel
import pandas as pd


class wechat_test():

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def get_friends_info(self):  # 获取好像信息，返回lis列表
        bot = Bot()
        lis = [['name', 'real_name', 'sex', 'city', 'province']]  # 把信息存储为一个二维列表,添加头部信息
        friend_all = bot.friends()

        for a_friend in friend_all:
            NickName = a_friend.raw.get('NickName', None)  # 获取所有好友信息 raw表示获取全部信息
            RemarkName = a_friend.raw.get('RemarkName', None)
            Sex = {1: "男", 2: "女", 0: "其他"}.get(a_friend.raw.get('Sex', None), None)
            City = a_friend.raw.get('City', None)
            Province = a_friend.raw.get('Province', None)
            Signature = a_friend.raw.get('Signature', None)
            # HeadImgUrl = a_friend.raw.get('HeadImgUrl', None)
            # HeadImgFlag = a_friend.raw.get('HeadImgFlag', None)
            list_0 = [NickName, RemarkName, Sex, City, Province, Signature]
            lis.append(list_0)
        return lis

    # 把lis信息写入到excle
    def friends_info_lis_to_excle(self):
        import openpyxl
        lis = self.get_friends_info()
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = self.sheetname
        for i in range(0, len(lis)):
            for j in range(0, len(lis[i])):
                sheet.cell(row=i + 1, column=j + 1, value=str(lis[i][j]))
        wb.save(self.filename)
        print("excel保存成功")

    # 参数为condition 词频，提取两个列表，condition 和 人数，降序列表
    def extract_data_as_two_lis(self, condition):
        df = read_excel(self.filename, sheet_name=self.sheetname)
        X_list = df[condition].fillna('0').tolist()  # 把列转换为list，用0替换Nan？
        counts = {}  # 创建字典
        for word in X_list:
            counts[word] = counts.get(word, 0) + 1  # 统计词频
        items = list(counts.items())  # 返回所有键值对
        items.sort(key=lambda x: x[1], reverse=True)  # 降序排序
        keylist = list()
        valueslist = list()
        for item in items:
            word, count = item
            # if word == '0':
            # word = "其他"
            keylist.append(word)  # 把词语降序word放进一个列表
            valueslist.append(count)
        return keylist, valueslist

    # 参数为 save_name 自动添加jpg 创建X条件词云,
    def city_wordcloud(self, save_name, condition):
        wordlist, giveup = self.extract_data_as_two_lis(condition)
        new_wordlist = list()
        try:
            for i in range(25):
                new_wordlist.append(wordlist[i])
        except:
            for i in range(10):
                new_wordlist.append(wordlist[i])
        wl = ' '.join(wordlist)  # 把列表转换成str wl为str类型，所以需要转换
        cloud_mask = np.array(Image.open("love.jpg"))  # 词云的背景图，需要颜色区分度高
        wc = WordCloud(
            background_color="black",  # 背景颜色
            mask=cloud_mask,  # 背景图cloud_mask
            max_words=100,  # 最大词语数目
            font_path='msyh.ttc',  # 调用font里的simsun.tff字体，需要提前安装
            height=500,  # 设置高度
            width=2600,  # 设置宽度
            max_font_size=1000,  # 最大字体号
            random_state=1000,  # 设置随机生成状态，即有多少种配色方案
        )
        myword = wc.generate(wl)  # 用 wl的词语 生成词云
        # 展示词云图
        plt.imshow(myword)
        plt.axis("off")
        # plt.show()
        try:
            wc.to_file(save_name + '.jpg')  # 把词云保存下当前目录（与此py文件目录相同）
            print("词云图保存成功")
        except:
            print("词云保存失败")

    # 参数为condition ,创建柱形html图片,
    def pillar_picture(self, condition, render_name):
        from pyecharts.charts import Bar
        from pyecharts.globals import ThemeType
        from pyecharts import options as opts

        keylist, valueslist = self.extract_data_as_two_lis(condition)
        new_keylist = list()
        new_valueslist = list()
        for i in range(10):
            new_keylist.append(keylist[i])
            new_valueslist.append(valueslist[i])
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        # x轴 列表
        bar.add_xaxis(new_keylist)
        bar.add_yaxis("好友分布", new_valueslist)
        # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
        # 也可以传入路径参数，如 bar.render("mycharts.html")
        bar.render(render_name)
        print("pillar_picture图片保存成功！")

    # 参数为condition,picture_name, keylist, valueslist, Map_condition->china或者广东创建html地图图片,图片名字为picture_name
    def map_picture(self, condition, picture_name, keylist, valueslist, Map_condition):
        from pyecharts import options as opts
        from pyecharts.charts import Map
        # from example.commons import Faker

        def map_visualmap() -> Map:
            new_keylist = list()
            new_valueslist = list()

            if condition == 'city':
                for i in range(len(keylist)):
                    # 列表处理,默认elsx里面的city没有'市'字，地图需要市字
                    new_keylist.append(keylist[i] + '市')
                    new_valueslist.append(valueslist[i])
            else:
                for i in range(len(keylist)):
                    new_keylist.append(keylist[i])
                    new_valueslist.append(valueslist[i])
            c = (
                Map()
                    .add("好友", [list(z) for z in zip(new_keylist, new_valueslist)], Map_condition)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
                    visualmap_opts=opts.VisualMapOpts(max_=200),
                )
            )

            try:
                c.render(picture_name)
            except:
                print("html地图图片创建失败")
            print('html地图图片保存成功')

        map_visualmap()  # 调用自己

    # 参数为condition，返回一个二维列表
    def find_friends_in_condition(self, condition):
        df = pd.read_excel(self.filename, usecols=[0, 1, 3], names=None)  # 不要列名
        df_li = df.values.tolist()
        name = list()
        for data in df_li:
            condition = condition
            if condition in data:
                name.append(data)
        self.map_picture()
        # print(len(name), name)
        return name


if __name__ == "__main__":
    wechat = wechat_test('wechat_info.xlsx', 'list')
    wechat.friends_info_lis_to_excle()
    wechat.city_wordcloud('city_wordclour', 'city')
    wechat.pillar_picture('city', 'render.html')
    keylist, valueslist = wechat.extract_data_as_two_lis('city')
    wechat.map_picture('city', 'test.html', keylist, valueslist, '广东')
    # wechat.find_friends_in_city()
