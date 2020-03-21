# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time


def next_page():
    try:
        wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'body > div.wrap.fix > div.box_read.clearfix > div.topp > div.topp_r.f-black > a:nth-child(6)'))).click()
    except:
        next_page()


#抓取每一页的信息
def getText():
    time.sleep(10)
    html = browser.page_source  # 得到网页源代码
    doc = pq(html)
    text1 = str(doc('.read_top').find('h1')) # 章节名字

    text2 = str(doc('#readcon')).replace('<br/>', '') # 正文去除br
    if text1!=None:
        print("正在獲取章節：{}".format(text1))
    return text1+text2

#把信息写入到text文本
def writeToText(text2):
    with open('text.txt', 'a', encoding="utf-8") as f:
        text2 = "".join([s for s in text2.splitlines(True) if s.strip()])  # 去空行
        f.write(text2.replace('<div class="txt fon_size" id="readcon">', '')) #去除多余字
    f.close()


time_start = time.time()
browser = webdriver.Chrome()
url = 'http://www.yuedyue.com/217_217828/70111118.html'
browser.get(url)
wait = WebDriverWait(browser, 10)

for i in range(0, 1178, 1):
    text = getText()  # 抓取信息
    writeToText(text)  # 寫入信息
    next_page()  # 下一頁

print('耗时：' + str(time.time() - time_start) + ' s')




# def getsource(url):
#     try:
#         s = requests.get(url)
#     except:
#         print('访问异常，跳过~！')
#     else:
#         s.encoding = 'gbk'
#         return s.text
#
#
# def getlist(url):
#     global txtname, txtzz
#     html = getsource(url)
#     ehtml = etree.HTML(html)
#     u = ehtml.xpath('//*[@id="list"]/dl/dd/a/@href')
#     t = ehtml.xpath('//*[@id="list"]/dl/dd/a/text()')
#     txtname = ehtml.xpath('//*[@id="info"]/h1/text()')[0].replace('\\', '').replace('/', '').replace(':', '').replace(
#         '*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
#     txtzz = ehtml.xpath('//*[@id="info"]/p[1]/text()')[0].replace('\xa0', '')
#     num = 0
#     for i in range(9, len(u)):
#         urllist.append(u[i] + '|' + t[i] + '|' + str(num))
#         num += 1
#
#
# def downtxt(url):
#     global downcount
#     u = url.split('|')[0]
#     t = url.split('|')[1]
#     num = url.split('|')[2]
#     content = ''
#     while len(content) == 0:
#         html = getsource(u)
#         ehtml = etree.HTML(html)
#         content = ehtml.xpath('string(//*[@id="content"])').replace('    ', '\r\n').replace('　　', '\r\n').replace(
#             '\xa0', '').replace('\ufffd', '').replace('\u266a', '').replace('readx;', '')
#     if os.path.exists(savepath + num + '.txt'):
#         print(num + '.txt 已经存在!')
#     else:
#         with codecs.open(savepath + num + '.txt', 'a')as f:
#             f.write('\r\n' + t + '\r\n' + content)
#         print(t + ' 下载完成!')
#         downcount += 1
#
#
# time_start = time.time();
# downcount = 0
# urllist = []
# getlist(url)
# savepath = os.getcwd() + '\\' + txtname + '\\'
# if os.path.exists(savepath) == False:
#     os.makedirs(savepath)
# pool = ThreadPool(multiprocessing.cpu_count())
# results = pool.map(downtxt, urllist)
# pool.close()
# pool.join()
# print('开始合并txt...')
# with codecs.open(savepath + txtname + '.txt', 'a')as f:
#     f.write(txtname)
#     f.write('\r\n')
#     f.write(txtzz)
#     f.write('\r\n')
#     for i in range(0, len(urllist)):
#         with open(savepath + str(i) + '.txt', "r") as fr:
#             txt = fr.read()
#             f.write(txt)
#             f.write('===========================')
#             fr.close()
#             os.remove(savepath + str(i) + '.txt')
# print('小说合并完成~！')
#
# print('')
# print('*' * 15 + ' 任务完成，结果如下：' + '*' * 15)
# print('')
# print('<' + txtname + '> 下载完成' + '，获取并下载章节页面：' + str(downcount) + ' 个')
# print('')
# print('耗时：' + str(time.time() - time_start) + ' s')
# print('')
# print('*' * 51)


# html = """</div>
# <div class="read_top">
# <h1>正文 第4章 再遭羞辱</h1>
# <p class="info">作者：范建明李倩倩&nbsp;<em class="pl10">更新时间：</em><span class="g3">2020-01-13 02:15</span><em class="pl10">字数：</em><span class="g3">1514字</span></p>
# </div>
# <div class="ad0 mt10 mb10 mx10"><script>ad728_1();</script></div>
# <div id="play" style="color:#f55;font-weight:bold;text-align:center"><div>一世强龙有声小说，阅读悦在线收听！</div></div>
# <div class="txt fon_size" id="readcon">
# &nbsp;&nbsp;&nbsp;&nbsp;李倩倩想好了，今天晚上做了一次之后，她一直要等到下个月，看看自己来不来例假。百度搜索，更多好看小说免费阅读。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;如果来了，她会让范建明再做一次。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;如果没来，就证明已经怀上了，如果怀上，李倩倩这辈子都不会再让范建明做了。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;换句话说，哪怕是结婚生子，李倩倩也只会跟范建明做这一次。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;范建明反而不着急，微笑着反问了一句：“如果我没猜错的话，你刚刚那张卡是方雅丹给你的，她之所以借给你那些钱，提出的条件，就是让你跟我结婚生子，对吗？”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;“不止如此。她一共借了我六十万，给了我一年的期限，如果我跟你生了孩子，这六十万就不用还了！”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;范建明倒吸了一口凉气：这不科学呀！虽然过去我也曾暗恋过方雅丹，可她从没正眼瞧我一下，怎么今天会为了我<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;范建明挠了挠后脑勺，忽然反应过来了。百度搜索，更多好看小说免费阅读。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;“你的意思是说，方雅丹也喜欢张国栋，所以”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;李倩倩白了范建明一眼，心里啐了一口：本来就被你恶心死了，还在装，你丫的是要让我恶心得永世不能超生吗？<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;就在这时，两辆越野车停在了他们面前，刘云坤带着一帮兄弟从车上下来了。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;“哟，还真是犯贱呀？几年不见，个头长高了，皮肤也黑了，身材倒也挺壮实，只是这犯贱的毛病怎么还没改呀？”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;说着，一身流氓气息的刘云坤，面带着冷笑，直接朝范建明走来。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;范建明看到刘云坤的那一瞬间，整个人都要爆了。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;但他还是强忍住了。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;他想看看李倩倩的反应。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;看到刘云坤带着人围了上来，李倩倩知道他们要干什么，却站在边上无动于衷。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;刚刚张国栋动手的时候，李倩倩之所以护着范建明，主要是为了让张国栋死心，所谓长痛不如短痛。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;这次则不然。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;刘云坤本来已经结婚，而且现在是社会上的混混，据说还是某一片区的老大。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;李倩倩对范建明恶心的不能再恶心了，心想，让刘云坤揍揍他也好，谁让他跟方雅丹合伙算计自己呢？<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;所以她没打算从中制止。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;看到刘云坤走到面前，范建明强压着怒火，像过去一样点头哈腰地笑道：“云坤，怎么这么巧？”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;“妈淡的，云坤也是你叫的吗？”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;没等刘云坤开口，他带来的兄弟飞起一脚，踢中了范建明的腰，范建明顺势向旁边踉跄了几步，还没站稳，另一个混混又是一脚踢中了他的胸口，范建明扑通一下仰面跌倒。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;他仰躺在地的时候，用眼角瞄了李倩倩一眼，发现李倩倩的脸偏到了一边。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;紧接着，其他几个混混一拥而上，照着范建明一顿拳打脚踢。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;医院的保安见状，赶紧冲出来拉架，有的还打电话报警。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;这些拳脚对于今天的范建明来说，已经无关痛痒，只是李倩倩的冷漠让他寒心。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;虽然方雅丹的做法不对，但只要李倩倩哪怕再多给他一点关爱，他就一定能像方雅丹所说的那样，让李倩倩彻底咸鱼翻身。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;可现在<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;看到保安过来拉架，还有人在报警，刘云坤走到范建明的面前，抬脚踩住他的脸说道：“臭小子，忘记了过去在学校的经历吗？记住了，从今天开始，老子见你一次揍一次，一直揍到你离开这座城市为止！”<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;说完，他又扬起腿，重重地踹了范建明胸口一脚，然后带着人离开了。<br />
# <br />
# &nbsp;&nbsp;&nbsp;&nbsp;范建明从地上爬起来之后，李倩倩才面无表情地看了他一眼，有些幸灾乐祸地说了一句：“刘云坤现在不得了，他可是社会上的老大，你可真要当心一点。”<br/>&nbsp;&nbsp;&nbsp;&nbsp;阅读悦,阅读悦精彩!<br/>&nbsp;&nbsp;&nbsp;&nbsp;(www.yuedyue.com = <a href='http://www.yuedyue.com'>阅读悦</a>)
# </div>
# <div class="ad ad3 mt10 mb10 mx10"><script>ad728_2();</script></div>
# <div class="read_dwn">
# <p class="f-gray6">(&larr;快捷键)<a href="http://www.yuedyue.com/217_217828/70110361.html">&lt;&lt;上一章</a><a href="http://www.yuedyue.com/217_217828/">目录</a><a href="http://www.yuedyue.com/217_217828/70110363.html">下一章>></a> (快捷键&rarr;)</p>
# </div>
# <div class="tc ad3"><script>ad728_3();</script></div>
# </div>
# <div class="side-s fr">
# <div class="boxs clearfix">
# <div class="t"><h2>本周强推</h2></div>
# <div class="qh">
# <dl class="ldt p10">
# """

#完成翻页动作

#翻转到下一页