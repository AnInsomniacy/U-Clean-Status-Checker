import json

import requests


def getStatus(postData):
    url = "https://phoenix.ujing.online/api/v1/wechat/devices/scanWasherCode"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBVc2VySWQiOiJvZ3lSVDF1M0dlZU9OV2N5SGdHekZYM3RoLVVNIiwiZXhwIjoxNjk0MDg5MTk5LCJpYXQiOjE2ODYwNTM5OTksImlkIjozMDE5NDgzMiwibmFtZSI6IjE5ODc2NTc2NzY4In0.AwDgYSsaDXMZ2NWCA5o0vEs_7MWOb1Tw-q0vH10OKXs",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=utf-8",
        "x-app-code": "BCI",
        "Origin": "https://wx.zhinengxiyifang.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002121) NetType/WIFI Language/zh_CN",
        "Referer": "https://wx.zhinengxiyifang.cn/",
        "x-app-version": "0.1.40",
        "Connection": "keep-alive",
    }

    data = {"qrCode": postData}

    response = requests.post(url, headers=headers, json=data)

    responseText = response.text

    response_dict = json.loads(responseText)
    canCreate = response_dict['data']['result']['createOrderEnabled']
    reason = response_dict['data']['result']['reason']
    return [canCreate, reason]


def returnStatus(urlList):
    result = ''
    for i in range(len(urlList)):
        result += '第 ' + str(i + 1) + ' 层洗衣机状态：'
        status = getStatus(urlList[i])
        if status[0]:
            result += '可以洗衣' + '\n\n'
        else:
            result += '不可以洗衣，原因：' + status[1] + '\n\n'
    return result