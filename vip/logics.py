from common.errors import PERM_ERROR
from lib.http import render_json

import logging

log = logging.getLogger('err')


class perm_require:
    # 权限检查修饰器
    def __init__(self, perm_id):
        self.prem_id = perm_id

    def __call__(self, func):
        def wrap(request):
            if request.user.vip.had_perm(self.prem_id):
                return func(request)
            else:
                print(request.user.nickname)
                log.error(f'{request.user.nickname} not has {self.prem_id}')
                return render_json(None, PERM_ERROR)
        return wrap
