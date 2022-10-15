from django.db import models
from django.db.models import Q
from user.models import User

class Swiper(models.Model):
    STATUS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢')
    )
    uid = models.IntegerField(verbose_name = '滑动者 UID')
    sid = models.IntegerField(verbose_name = '被滑动者 UID')
    status = models.CharField(max_length = 10, choices=STATUS)
    time = models.DateTimeField(auto_now_add = True)

    @classmethod
    def mark(cls, uid ,sid, status):
        defaults = {'status': status}
        cls.objects.update_or_create(uid = uid, sid = sid, defaults = defaults)

    @classmethod
    def is_like(cls, uid, sid):
        return cls.objects.filter(uid=uid, sid=sid,
                           status__in=['like', 'superlike']).exists()

class Friend(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        Friend.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def break_off_friends(cls, uid1, uid2):
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        try:
            cls.objects.get(uid1 = uid1, uid2 = uid2).delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def is_friend(cls, uid1, uid2):
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()

    @classmethod
    def friends(cls, uid):
        condition = Q(uid1=uid) | Q(uid2=uid)
        sids = [friend.uid2 if friend.uid1 == uid else friend.uid1
                for friend in cls.objects.filter(condition)]
        return User.objects.filter(id__in = sids)