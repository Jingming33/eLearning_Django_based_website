#  fake sending sms function, for self checking on web page

import json
from apps.utils.random_str import generate_random


def send_single_sms(apikey, code, mobile):
    """
    :param client:
    :param mobile:
    :return:
    """

    text = 'Your verification code is {}, Please ignore this message if it is not my operation'.format(code)

    # response_data = {
    #     'apikey': apikey,
    #     'mobile': mobile,
    #     'text': text
    # }
    #
    # res = json.dumps(response_data)
    # re_json = json.loads(res)

    '''return fake json'''
    '''
        {
        "code": 0,
        "msg": "success",
        "count": 1,
        "fee": 0.05,
        "unit": "RMB",
        "mobile": "13200000000",
        "sid": 3310228982
    }
    '''

    re_json = {
        'code': 0,
        'status': 'success',
    }
    return re_json


# if __name__ == '__main__':
#     print(send_single_sms('123', generate_random(4, 0), '123455678'))
