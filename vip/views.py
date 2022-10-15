from lib.http import render_json
from user.models import User


def modify_vip(request):
    user = request.user
    vip_id = request.POST.get('vip_id')
    user.__dict__.update(vip_id = vip_id)
    user.save()
    return render_json(None)

def get_vip(request):
    vip_level = request.user.vip.level
    return render_json(vip_level)


