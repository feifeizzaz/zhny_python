#coding=utf-8
import requests
import json

#'categoryId': "-12",  肉单
#'categoryId': "-11",  清仓
#'categoryId': "15",  百货
#'categoryId': "1",  食品
#'categoryId': "13",  水果

headers = {
    'authority': "jinbao.pinduoduo.com",
    'path': "/network/api/common/goodsList",
    'method': "POST",
    'scheme': "https",
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    # 'content-length': "480",
    'content-type': "application/json;charset=UTF-8",
    'cookie': "_pati=lVytuRobqC5E7uePM2Knzb8uCChWxwag; _nano_fp=Xpdbn0UyXqPbn5Tql9_MNKYTFbdPQGQ0wIoiSVZo; api_uid=rBUUNV8RDlFq7QefrP8TAg==; DDJB_PASS_ID=de3debe90521e232d8497bc36dacf5be",
    'origin': "https://jinbao.pinduoduo.com",
    'referer': "https://jinbao.pinduoduo.com/promotion/single-promotion",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

class getjs1():
    def getjs():
        url = "https://jinbao.pinduoduo.com/network/api/common/goodsList"

        #爬取拼多多商品列表数据
        payload = {
            'crawlerInfo': "0anAfxnpyNQo59mRsgZGrkhE2I59x_oOAc3uAtGXwgnTZ4CS4N-8EKda5IE46iiZsR7QVZWp_b8xAdcckH2TlYD3cZdznK7FFPfOjZy4fuvveT8IhcFmaUDKN2bc5Xzp-GzDIgykynKULcFq5rqyWUq9XbwO1a07u_V974sOGIYQXbbwPTCqPHrw51dwNoQ-B4Vr2UYYstZBH9yz-AE4VtSPsITdPzKbG3tKk2d4fvxxwGcowMkfGz5FvnHKEglBoT7HgAvtCW-KGXHuIF0m6n-2bONZEuppPF0cOCkCuRsVr2hJDcZxnwXxD3c7Xb4VozJj7im0KLDlnXIV7H1zeUzhFRkzrSvq4BlpoFqt98ofsLgzRyDCqE3FHybUm1mh2qM-b6Xi7_pwwi0EWNOiZ0pYDC8fhHMSxAhLrk-uNzRYqre96sj",
            'keyword': "",
            'pageSize': "60"
            }

        #发送post请求
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        filename='goodslist.json'
        with open(filename,'w') as file_obj:
            file_obj.write(response.text)

    def getjs_rd(categoryId,pageNumber,json_name):
        url = "https://jinbao.pinduoduo.com/network/api/common/goodsList"

        #爬取拼多多商品列表数据
        payload = {
            'categoryId': "-12",
            'crawlerInfo': "0anAfxnpyNQo59mRsgZGrkhE2I59x_oOAc3uAtGXwgnTZ4CS4N-8EKda5IE46iiZsR7QVZWp_b8xAdcckH2TlYD3cZdznK7FFPfOjZy4fuvveT8IhcFmaUDKN2bc5Xzp-GzDIgykynKULcFq5rqyWUq9XbwO1a07u_V974sOGIYQXbbwPTCqPHrw51dwNoQ-B4Vr2UYYstZBH9yz-AE4VtSPsITdPzKbG3tKk2d4fvxxwGcowMkfGz5FvnHKEglBoT7HgAvtCW-KGXHuIF0m6n-2bONZEuppPF0cOCkCuRsVr2hJDcZxnwXxD3c7Xb4VozJj7im0KLDlnXIV7H1zeUzhFRkzrSvq4BlpoFqt98ofsLgzRyDCqE3FHybUm1mh2qM-b6Xi7_pwwi0EWNOiZ0pYDC8fhHMSxAhLrk-uNzRYqre96sj",
            'keyword': "",
            'pageNumber': 2,
            'pageSize': "60"
            }
        #将参数的值传给字典
        payload['categoryId']=categoryId
        payload['pageNumber']=pageNumber

        print(payload)

        #发送post请求
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        #按函数传入的参数创建json名称
        with open(json_name,'w') as file_obj:
            file_obj.write(response.text)

#getjs1.getjs_rd('11',7,'aaacs.json')