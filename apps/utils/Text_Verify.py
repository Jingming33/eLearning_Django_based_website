# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-29 16:31

import requests
import nexmo


def send_single_sms(client, mobile):
    # sending single smg

    #  sending from yunpian
    # url = ''
    # text = 'Your verification code is {}, Please ignore this message if it is not my operation'.format(code)
    # res = requests.post(url, data={
    #     'apikey': apikey,
    #     'mobile': mobile,
    #     'text': text
    # })
    #
    # return res

    #  sending from nexmo
    __client = client
    __mobile = mobile
    response_data = __client.send_message({
        'from': 'Nexmo',
        'to': __mobile,
        'text': 'Hello from Jingming, Hahaha, xiao feifei',
    })

    return response_data


# if __name__ == '__main__':
#     send_single_sms()

# if __name__ == '__main__':
#     res = send_single_sms('', '123456', '13908062965')
#     import json
#     res_json = json.loads(res.text)
#     code = res_json['code']
#     msg = res_json['msg']
#     if code ==0:
#         print('success')
#     else:
#         print('sending failed: {}'.format(msg))
#
#     print(res.text)
