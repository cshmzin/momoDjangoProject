from lib.http import render_json
from swiper.logics import get_rcmd_users, like_logic, superlike_logic, dislike_logic, rewind_logic
from swiper.models import Friend


# Create your views here.
from vip.logics import perm_require
import logging

log = logging.getLogger('inf')


def users(request):
    # 获取推荐列表
    group_num = request.GET.get('group_num', 0)
    start = int(group_num) * 5
    end = start + 5
    users = get_rcmd_users(request.user)[start:end] # 惰性加载

    result = [user.to_dict() for user in users]
    return render_json(result)

def like(request):
    # 喜欢
    sid = int(request.POST.get('sid'))
    if_matched = like_logic(request.user, sid)
    log.info(f'{str(request.user.id)} like {str(sid)}')
    return render_json({'if_matched': if_matched})

@perm_require('superlike')
def superlike(request):
    # 超级喜欢(Vip特权)
    sid = int(request.POST.get('sid'))
    if_matched = superlike_logic(request.user, sid)
    log.info(f'{str(request.user.id)} superlike {str(sid)}')
    return render_json({'if_matched': if_matched})

def dislike(request):
    # 不喜欢
    sid = int(request.POST.get('sid'))
    dislike_logic(request.user, sid)
    log.info(f'{str(request.user.id)} dislike {str(sid)}')
    return render_json(None)

@perm_require('rewind')
def rewind(request):
    # 反悔(Vip特权)
    sid = int(request.POST.get('sid'))
    rewind_logic(request.user, sid)
    return render_json(None)

def friends(request):
    my_friends = Friend.friends(request.user.id)
    friends_info = [frd.to_dict() for frd in my_friends]
    return render_json({'friends_info':friends_info})



