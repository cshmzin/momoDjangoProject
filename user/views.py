from django.views.decorators.csrf import csrf_exempt

from common.errors import VCODE_ERRORS, PROFILE_ERRORS
from lib.http import render_json
from user.logics import send_sms, check_vcode

from user.models import User
from user.forms import ProfileForm


def get_verify_code(request):
    # 手机注册
    phonenum = request.GET.get('phonenum')
    send_sms(phonenum)
    return render_json(None)


def login(request):
    # 短信验证登录
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, _ = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        print(request.session.get('uid'))
        return render_json(user.to_dict())
    else:
        return render_json(None, VCODE_ERRORS)

def get_profile(request):
    # 获取个人资料
    user = request.user
    return render_json(user.profile.to_dict())

def modify_profile(request):
    # 修改个人资料
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.clean())
        user.profile.save()
        return render_json(None)
    else:
        return render_json(form.errors, PROFILE_ERRORS)


def upload_avater(request):
    # 上传头像
    pass