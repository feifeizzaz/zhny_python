from selenium import webdriver
import requests
from lxml import etree
import pymysql
import time

#创建浏览器对象
browser = webdriver.Chrome(r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
browser.get("https://www.cnhnb.com/login/") # Load page

#用户登录
browser.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div[2]/div[3]/span[2]").click()
browser.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div[2]/div[1]/div[1]/input").send_keys('13720280847')
browser.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div[2]/div[1]/div[2]/input").send_keys('zcf8277623')
browser.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div[2]/div[4]/button").click()
time.sleep(1)

url = "https://www.cnhnb.com/hangqing/cdlist-200319"

#反爬虫
pm_list=[]
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"

#将数据存到数据库中
def save_data(dq_lx_list,pm_list,cd_list,jg_list,dw_list,sj_list,fbsj_list,lx_i):
    #conn = pymysql.connect(host='192.168.10.150', user='nswy', password='1234', db='nswy_dev')  # 建立数据库链接
    conn = pymysql.connect(host='rm-bp192r5c21ppj65e2lo.mysql.rds.aliyuncs.com', user='dbzhny', password='s7K1ipQdB#476825', db='iashop')  # 建立数据库链接
    mycursor = conn.cursor()
    #去掉单位中的数字
    for i in range(10):
        dw_list = [x.replace(str(i),'').replace('.','') for x in dw_list]
    #print(jg_list)
    #print(dw_list)
    '''
 sql = ' CREATE TABLE hnw_scjg
 (id int primary key auto_increment COMMENT '主键',
 lx VARCHAR(20) COMMENT '类型',
 pm VARCHAR(20) COMMENT '品名',
 cd VARCHAR(100) COMMENT '产地规格',
 jg float COMMENT '价格数值',
 dw VARCHAR(100) COMMENT '单位',
 sj VARCHAR(100) COMMENT '升降',
 fbsj VARCHAR(40) COMMENT '发布时间') DEFAULT CHARSET = UTF8MB4' #创建表格
    '''
    # mycursor.execute(sql)
    for id,pm in enumerate(pm_list):  #enumerate可以把原来的列表变为索引和元素一一配对，第一个是0
        if id>0:
            sql = "INSERT INTO hnw_scjg(lx,pm,cd,jg,dw,sj,fbsj) VALUES(%s,%s,%s,%s,%s,%s,%s)"   # %s是占位符   strip函数去掉占位符
            mycursor.execute(sql,(dq_lx_list[lx_i].strip(),pm_list[id].strip(),cd_list[id].strip(),jg_list[id].strip(),dw_list[id].strip(),sj_list[id].strip(),fbsj_list[id].strip()))  #执行sql,id,movie添加到对应的占位符中去
    conn.commit()  #对数据库表格中的数据做了修改必须提交生效
    mycursor.close()
    conn.close()  #关闭数据库连接

#解析网站获取的内容取出字段
def parse_html(htmlfile,lx_i):
    global pm_list
    global html_browser
    browser.get(htmlfile)  # Load page
    html_browser = browser.page_source
    html = etree.HTML(html_browser)  # 分析HTML，返回DOM根节点
    dq_lx_list = html.xpath("//li[@class='first-cate-item']//a/text()") #当前类型
    pm_list = html.xpath("//span[@class='product']/text()")  # 返回品名list
    cd_list = html.xpath("//span[@class='place']/text()")  # 返回产地规格list
    jg_list = html.xpath("//span[@class='price']/text()")  # 返回最高价list
    dw_list=jg_list  #把价格给单位
    sj_list = html.xpath("//span[5]/text()")  # 返回最低价list
    fbsj_list = html.xpath("//span[@class='time']/text()")  # 返回均价list
    sl=len(pm_list)
    print(pm_list)

    save_data(dq_lx_list, pm_list, cd_list, jg_list, dw_list, sj_list, fbsj_list, lx_i)

#循环爬取每一页的数据
for lx_i in range(1,18):
    if lx_i>9:
        url="https://www.cnhnb.com/hangqing/cdlist-200320"
        i=lx_i-10
    else:
        i=lx_i
    for ym_i in range(1,100):
        #time.sleep(3)  #休息5秒钟
        url_hb = url + str(i) + "-0-17-0-0-" +  str(ym_i)
        print(url_hb)
        parse_html(url_hb,lx_i)
        print(len(pm_list))
        if len(pm_list)<16:
            break





