#coding=utf-8
import os
import json
import ddjb_getjs
import pymysql
import time

#'categoryId': "-12",  肉单
#'categoryId': "-11",  清仓
#'categoryId': "15",  百货
#'categoryId': "1",  食品
#'categoryId': "13",  水果
#
lm_mc='水果'
dict_lm={'肉单':'-12','清仓':'-11','百货':'15','食品':'1','水果':'13'}
id_name_key = [k for k, v in dict_lm.items()]
print("遍历字典把所有的key取出来:", id_name_key)
for key in dict_lm:
    print(key)
#lm=dict_lm[lm_mc]
#print(lm)

#保存数据
def save_data(fy,lm_mc,dict_data):
    conn = pymysql.connect(host='rm-bp192r5c21ppj65e2lo.mysql.rds.aliyuncs.com', user='dbzhny', password='s7K1ipQdB#476825', db='mall_cs')  # 建立数据库链接
    mycursor = conn.cursor()
    #sql_csh = "DELETE FROM pdd_rxsp"  # %s是占位符   strip函数去掉占位符
    #mycursor.execute(sql_csh)

    for id, pm in enumerate(dict_data.get('result').get('goodsList')):  # enumerate可以把原来的列表变为索引和元素一一配对，第一个是0
        sql = "INSERT INTO pdd_rxsp(ym,lm,pm,splx,scj,yhjje,zhj,xl,shopname,yjbl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # %s是占位符   strip函数去掉占位符
        mycursor.execute(sql, (
        fy, lm_mc, pm.get('goodsName'),pm.get('categoryName'), str(pm.get('minGroupPrice')/1000),str(pm.get('couponDiscount')/1000),
        str((pm.get('minGroupPrice') - pm.get('couponDiscount')) / 1000), pm.get('salesTip'), pm.get('mallName'),str(int(pm.get('promotionRate')/10))+'%'))  # 执行sql,id,movie添加到对应的占位符中去
        print(id,'页码:'+str(fy),'类目:'+lm_mc,'商品名称：'+pm.get('goodsName'),'原价：'+str(pm.get('minGroupPrice')/1000)+'元','优惠券金额：'+str(pm.get('couponDiscount')/1000)+'元',
              '折后价：'+str((pm.get('minGroupPrice')-pm.get('couponDiscount'))/1000)+'元','商品销量：'+pm.get('salesTip'),'店铺名称：'+pm.get('mallName'),
              '商品类型：'+pm.get('categoryName'),
              '佣金比率：' +str(int(pm.get('promotionRate')/10))+'%'+';')
    conn.commit()  #对数据库表格中的数据做了修改必须提交生效
    mycursor.close()
    conn.close()  #关闭数据库连接
#生成json文件
for key in  dict_lm:
    for fy in range(1,5):#翻页循环
        print(dict_lm[key])
        ddjb_getjs.getjs1.getjs_rd(dict_lm[key],fy,'aaacs.json')

        #ddjb_getjs.getjs1.getjs()
        p = r'C:\workspase\pythonworkspase\zhny\pdd'+r'\aaacs.json'
        #判断是否存在json文件，如果存在则把json文件中的内容转换为字典存到dict_data中
        if os.path.exists(p):
            f = open(p, 'r',encoding = 'utf-8')
            dict_data = json.load(f)

        print(dict_data)
        #查看商品数量#60
        #print(len(dict_data.get('result').get('goodsList')))
        #调用保存数据函数
        #save_data(fy, lm_mc, dict_data)
        save_data(fy, key, dict_data)
        time.sleep(5)
    #print(dict_data.get('result').get('goodsList')[0].get('goodsName'))

'''
 sql = '  CREATE TABLE pdd_rxsp
 (id int primary key auto_increment COMMENT '主键',
  ym VARCHAR(20) COMMENT '页码',
	lm VARCHAR(10) COMMENT '类目',
	splx VARCHAR(10) COMMENT '商品类型',
	pm VARCHAR(20) COMMENT '商品名称',
	scj VARCHAR(20) COMMENT '市场价',
	yhjje VARCHAR(20)  COMMENT '优惠金额',
	zhj VARCHAR(20) COMMENT '折后价',
	yjbl VARCHAR(20) COMMENT '佣金比例',
	xl VARCHAR(10) COMMENT '销量',
	shopname VARCHAR(40) COMMENT '店铺名称'，
	`CreateTime` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
	) DEFAULT CHARSET = UTF8MB4 COMMENT = '拼多多热销商品查询'' #创建表格
'''

    # for id, pm in enumerate(dict_data.get('result').get('goodsList')):  # enumerate可以把原来的列表变为索引和元素一一配对，第一个是0
    #     print(id,'页码:'+str(fy),'类目:'+lm_mc,'商品名称：'+pm.get('goodsName'),'原价：'+str(pm.get('minGroupPrice')/1000)+'元','优惠券金额：'+str(pm.get('couponDiscount')/1000)+'元',
    #           '折后价：'+str((pm.get('minGroupPrice')-pm.get('couponDiscount'))/1000)+'元','商品销量：'+pm.get('salesTip'),'店铺名称：'+pm.get('mallName'),
    #           '商品类型：'+pm.get('categoryName'),
    #           '佣金比率：' +str(int(pm.get('promotionRate')/10))+'%'+';')

# goodsName  商品名称
# salesTip  销量
# mallName  店铺名称
# categoryName  分类名称
# promotionRate  折扣
# couponDiscount 优惠券
# couponTotalQuantity 优惠券总共数量
# couponRemainQuantity 优惠券剩余数量
# couponStartTime 优惠券活动开始时间
# couponEndTime 优惠券活动结束时间
# minGroupPrice 商品原价