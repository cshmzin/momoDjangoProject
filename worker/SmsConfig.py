import time
from unisdk.sms import UniSMS
from unisdk.exception import UniException

## 短信接口配置
HY_SMS_URL = "https://106.ihuyi.com/webservice/sms.php?method=Submit"

HY_SMS_PARAMS = {
    'account': 'C83850006',
    'password': 'e2cea0e05f9bf2c76789bcde46207958',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    #'content': '恭喜你获得本公司的筛选，您的简历序号为%s。请在2022年10月14日18：00之前，点击以下链接自主选择面试时间https://ripshun.com/。',
    'mobile': None,
    'format' : 'json'
}

# clinet = UniSMS("m8aRWBaMGJcfPjzQ8r8asiZXQaLob1FLuQi5LS9SZi2ok5YTc",)
# SMS_PARAMS = {
#     "to": None,
#     "signature": "UniSMS",
#     "content": "您的验证码是%s, 2分钟内有效。",
#     "templateData": {
#         "code": 7777
#     }
# }

