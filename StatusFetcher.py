import json

import requests

from GlobalVar import Global_Bearer


def getStatus(postData):
    url = "https://phoenix.ujing.online/api/v1/wechat/devices/scanWasherCode"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer " + Global_Bearer,
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
    # 如果code是401，说明token过期了，需要重新登录
    if response_dict['code'] == 401:
        return [False, 'token过期，无法获取状态，请等待作者更新']
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
