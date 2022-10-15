from django.db import models

class Vip(models.Model):
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField()
    price = models.FloatField()

    def perms(self):
        # 当前Vip具有的所有权限
        relations = VipPermRelation.objects.filter(vip_id=self.id)
        perm_id_list = [relation.perm_id for relation in relations]
        return Permission.objects.filter(id__in = perm_id_list)

    def had_perm(self, perm_name):
        # 检查是否含有某权限
        perm = Permission.objects.get(name=perm_name)
        return VipPermRelation.objects.filter(vip_id=self.id, perm_id=perm.id).exists()

class Permission(models.Model):
    '''
    权限表
        会员身份标识
        超级喜欢
        返回功能
        任意更改定位
        无限喜欢次数
    '''
    name =  models.CharField(max_length=32, unique=True)

class VipPermRelation(models.Model):
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()

