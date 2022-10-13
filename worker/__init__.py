'''
初始化，将django与celery绑定
'''
import os
from celery import  Celery


## 设置环境变量，加载Django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

# 创建 Celery Application
celery_app = Celery('swiper')
celery_app.config_from_object('worker.CeleryConfig')
celery_app.autodiscover_tasks() #自动加载django任务

def call_by_worker(func):
    # 将任务放在Celery中异步执行
    '''
    主要执行以下功能
    tesk = celery_app.task(tesk)
    tesk.delay(x,y)
    '''
    task = celery_app.task(func)
    return task.delay


