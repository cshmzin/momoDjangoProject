from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from common.errors import VCODE_ERRORS
from lib.http import render_json
from user.logics import send_sms, check_vcode
from django.core.cache import cache
import json
from django.http import JsonResponse
# Create your views here.
from user.models import User


def get_verify_code(request):
    # 手机注册
    phonenum = request.GET.get('phonenum')
    send_sms(phonenum)
    return render_json(None, 0)


@csrf_exempt
def login(request):
    # 短信验证登录
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, _ = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        age = user.age
        profile = user.profile.to_dict()
        print(age, profile)
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, VCODE_ERRORS)

def get_profile(request):
    # 获取个人资料
    pass

def modify_profile(request):
    # 修改个人资料
    pass

def upload_avater(request):
    # 上传头像
    pass