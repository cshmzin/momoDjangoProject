from django import forms
from user.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段[字段1,字段2,]
        exclude = None  # 排除的字段
        labels = None  # 提示信息以 {字段名:label名}的形式
        help_texts = None  # 帮助提示信息
        widgets = None  # 自定义插件以
        error_messages = None  # 自定义错误信息

    def clean_max_age(self):
        '''
        自定义校验(钩子， clean_***, *** 为要验证的字段名)
        1. 函数名为“clean_字段名”或者“clean”
        2. 数据校验有误，只能抛ValidationError异常，因为在源码中捕获ValidationError异常
        3. 数据校验成功，返回数据
        :return:
        '''
        min_dating_age = self.cleaned_data['min_age']
        max_dating_age = self.cleaned_data['max_age']
        print(max_dating_age, min_dating_age)
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age > max_dating_age')
        return max_dating_age