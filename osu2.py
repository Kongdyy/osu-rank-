from urllib import request
from bs4 import BeautifulSoup as bs
import bs4
import tkinter
import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

'''conn = sqlite3.connect("D:/osutest.db")

sqlstr = "create table user (\
          rankid varchar(5) primary key, \
          playername varchar(25),\
          playercounter varchar(25),\
          performance varchar(10),\
          playcount varchar(10)\
          )"
conn.execute(sqlstr)'''


'''def main(plist,html_data,num):
    tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}\t{4:^10}"
    win = tkinter.Tk()
    win.title('osu！前五十名查询')
    win.geometry('600x300')
    btn1 = Button(win,text="爬取并存储数据",command=FillPlayerList(plist,html_data))
    btn2 = Button(win,text="打印数据",command=PrintPlayerList(plist,num))
    t1 = '排名     名称      国家         成绩        游戏次数'
    t2 = plist
    btn1.pack()
    btn2.pack()
    win.mainloop()'''
#获取网站页面
def GetHtmlText(url):
    try:
        resp = request.urlopen(url)
        html_data = resp.read().decode('utf-8')
        return html_data
    except:
        return ""
#抓取需要的信息
def FillPlayerList(plist,html_data):

    soup = bs(html_data,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            spans=tr('span')
            plist.append([  tds[0].string,spans[1].string,spans[0].get('title'),tds[4].string,tds[3].string])

'''def PrintPlayerList(plist,num):
    #tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}\t{4:^10}"
    #print(tplt.format("排名","名称","国家","成绩","游戏次数"))
    #t1=tplt.format("排名","名称","国家","成绩","游戏次数")
    for i in range(num):
        p = [x.strip() for x in plist[i]]
        #print(tplt.format(p[0],p[1],p[2],p[3],p[4]))'''


if __name__=='__main__':
    player = []
    url ='https://osu.ppy.sh/rankings/osu/performance'
    html_data=GetHtmlText(url)
    FillPlayerList(player,html_data)
    #PrintPlayerList(player, 15)



