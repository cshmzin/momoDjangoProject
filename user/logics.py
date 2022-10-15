import time

import requests

from common.errors import SEND_SMS_ERRORS
from lib.http import render_json
from worker import SmsConfig
import random
from worker import call_by_worker
from django.core.cache import cache


def gen_verify_code(length = 6):
    '''
    生成验证码
    :param length: 验证码长度
    :return: 验证码
    '''
    # return random.randint(10 ** (length - 1), 10 ** length)
    return 1

#@call_by_worker
def send_sms(phonenum):
    '''
    发送消息
    :param phonenum: 手机号
    :return: response
    '''
    vcode = gen_verify_code()
    cache.set('VerifyCode' + str(phonenum), vcode, 1200)
    print(phonenum, vcode)
    # sms_cfg = SmsConfig.HY_SMS_PARAMS.copy()
    # sms_cfg['content'] = sms_cfg['content'] % vcode
    # sms_cfg['mobile'] = phonenum
    # response = requests.post(SmsConfig.HY_SMS_URL, data = sms_cfg)

def check_vcode(phonenum, vcode):
    '''

    :param phonenum:
    :param vcode:
    :return:
    '''
    cache_vcode = cache.get('VerifyCode' + str(phonenum))
    if str(vcode) == str(cache_vcode):
        return True
    else:
        return False

if __name__ == '__main__':
    send_sms('15629421629')