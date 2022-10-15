from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from lib.http import render_json
from user.models import User
from common import errors


class AuthMiddlewareMixin(MiddlewareMixin):
    # 用户登陆验证中间价
    WHITE_LIST = [
        '/user/verify',
        '/user/login',
    ]
    def process_request(self, request):
        # 如果请求的URL在白名单内，直接跳过检查
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return

        # 进行登录检查
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id = uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, errors.LOGIN_ERRORS)
        # return redirect('/user/login/')