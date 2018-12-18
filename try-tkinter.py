from urllib import request
from bs4 import BeautifulSoup as bs
import bs4
import sqlite3
import os
from tkinter import Tk, Label, StringVar, Button, LEFT


def main(plist, html_data, num):
    win = Tk()
    win.title('osu！前五十名查询')
    win.geometry('600x300')
    text = StringVar()
    label = Label(win, justify=LEFT, textvariable=text)
    btn1 = Button(win, text="爬取并存储数据",
                  command=FillPlayerList(plist, html_data))
    btn2 = Button(win, text="打印数据", command=PrintPlayerList(plist, num, text))
    btn1.pack()
    btn2.pack()
    label.pack()
    win.mainloop()

# 获取网站页面
def GetHtmlText(url):
    try:
        resp = request.urlopen(url)
        html_data = resp.read().decode('utf-8')
        return html_data
    except:
        return ""


# 抓取需要的信息
def FillPlayerList(plist, html_data):
    soup = bs(html_data, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            spans = tr('span')
            plist.append([tds[0].string, spans[1].string, spans[0].get(
                'title'), tds[4].string, tds[3].string])


def PrintPlayerList(plist, num, text):
    plist = [[y.strip() for y in x] for x in plist]
    tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}\t{4:^10}"
    lines = []
    lines.append(tplt.format("排名", "名称", "国家", "成绩", "游戏次数"))
    for p in plist:
        lines.append(tplt.format(p[0], p[1], p[2], p[3], p[4]))
    lines_text = '\n'.join(lines)
    text.set(lines_text)


if __name__ == '__main__':
    player = []
    url = 'https://osu.ppy.sh/rankings/osu/performance'
    html_data = GetHtmlText(url)
    main(player, html_data, 15)
