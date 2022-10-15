from django.db.models import Q

from user.models import User
from swiper.models import Swiper, Friend
import datetime

def get_rcmd_users(user):
    dating_sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_age
    max_age = user.profile.max_age

    current_year = datetime.date.today().year
    min_year = current_year - min_age
    max_year = current_year - max_age

    users = User.objects.filter(sex = dating_sex, location = location,
                        birth_year__gte = max_year,
                        birth_day__lte = min_year)
    return users

def like_logic(user, sid):
    Swiper.mark(user.id, sid, 'like')
    if Swiper.is_like(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False

def superlike_logic(user, sid):
    Swiper.mark(user.id, sid, 'superlike')
    if Swiper.is_like(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False

def dislike_logic(user, sid):
    Swiper.mark(user.id, sid, 'dislike')

def rewind_logic(user, sid):
    # 撤销滑动记录
    try:
        Swiper.objects.get(uid = user.id, sid = sid).delete()
    except Swiper.DoesNotExist:
        pass
    # 撤销好友关系
    Friend.break_off_friends(user.id, sid)







