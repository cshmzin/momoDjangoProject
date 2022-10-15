import os
import random

import django

import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 定位到你的django根目录
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

django.setup()

from vip.models import Permission, Vip, VipPermRelation
def create_perission():
    perission_names = [
        'vipflag',
        'superlike',
        'rewind',
        'anylocation',
        'unlimit_like'
    ]
    for name in perission_names:
        Permission.objects.get_or_create(name = name)

def create_vip():
    for i in range(4):
        Vip.objects.get_or_create(
            name='会员-%d' % i,
            level = i,
            price = i * 5.0
        )

def create_vip_prem_relations():
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    vipflag = Permission.objects.get(name='vipflag')
    superlike = Permission.objects.get(name='superlike')
    rewind = Permission.objects.get(name='rewind')
    anylocation = Permission.objects.get(name='anylocation')
    unlimit_like = Permission.objects.get(name='unlimit_like')

    VipPermRelation.objects.create(vip_id=vip1.id, perm_id=vipflag.id)
    VipPermRelation.objects.create(vip_id=vip1.id, perm_id=superlike.id)

    VipPermRelation.objects.create(vip_id=vip2.id, perm_id=vipflag.id)
    VipPermRelation.objects.create(vip_id=vip2.id, perm_id=rewind.id)

    VipPermRelation.objects.create(vip_id=vip3.id, perm_id=vipflag.id)
    VipPermRelation.objects.create(vip_id=vip3.id, perm_id=superlike.id)
    VipPermRelation.objects.create(vip_id=vip3.id, perm_id=rewind.id)
    VipPermRelation.objects.create(vip_id=vip3.id, perm_id=anylocation.id)
    VipPermRelation.objects.create(vip_id=vip3.id, perm_id=unlimit_like.id)

if __name__ == '__main__':
    create_perission()
    create_perission()
    create_vip_prem_relations()