#!/usr/bin/env python

from pathlib import Path
import sys
import os
import random

import django

import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 定位到你的django根目录
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

django.setup()

from user.models import User
from faker import Faker


faker=Faker(locale="zh_CN")

for i in range(1000):
    name, pn = faker.name(), faker.phone_number()
    User.objects.create(
        nickname = name,
        phonenum = pn,
        sex = random.choice(['男', '女']),
        birth_year = random.randint(1980, 2000),
        birth_month = random.randint(1, 12),
        birth_day = random.randint(1, 28),
        location = random.choice(['北京', '上海', '深圳', '成都', '广州', '西安', '武汉'])
    )
    print('created: %s %s' % (name, pn))