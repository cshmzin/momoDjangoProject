from common.errors import PERM_ERROR
from lib.http import render_json


class perm_require:
    def __init__(self, perm_id):
        self.prem_id = perm_id

    def __call__(self, func):
        def wrap(request):
            if request.user.vip.had_perm(self.prem_id):
                return func(request)
            else:
                return render_json(None, PERM_ERROR)
        return wrap
