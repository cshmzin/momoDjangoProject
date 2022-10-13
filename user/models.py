from django.db import models
import datetime
from django.utils.functional import cached_property

# Create your models here.
# unique 设置唯一
# ImageField:记录文件的路径
from lib.orm import ModelMixin


class User(models.Model, ModelMixin):
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    nickname = models.CharField(max_length=16, unique=True) # max_length可多一点不要少一点，如果超过会截断
    phonenum = models.CharField(max_length=15, unique=True) #
    sex = models.CharField(default='男', max_length=8, choices=SEX)
    birth_year = models.IntegerField(default=2022)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(default='无', max_length=256) # 图像
    location = models.CharField(default='无', max_length=32) # 位置

    @cached_property
    # 只读属性,实际上每次调用都是函数。
    def age(self):
        today = datetime.date.today()
        # datatime.date 只包含日期
        # datatime.time 只包含时间
        # datatime.datetime 包含日期和时间
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_date).days // 365

    @property
    def profile(self):
        # 用户配置项关联
        # 一对一关联
        # if 'my_profile' not in self.__dict__:
        if not hasattr(self, 'my_profile'):
            my_profile, _ = Profile.objects.get_or_create(id=self.id)
            self.my_profile = my_profile
        return self.my_profile


class Profile(models.Model, ModelMixin):
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    '''用户配置项'''
    dating_sex = models.CharField(default='女', max_length=8, choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查询范围')
    max_distance = models.IntegerField(default=10, verbose_name='最小查询范围')

    min_age = models.IntegerField(default=18, verbose_name='最小年龄')
    max_age = models.IntegerField(default=45, verbose_name='最大年龄')


    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_match = models.BooleanField(default=True, verbose_name='不让不匹配的看相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')

