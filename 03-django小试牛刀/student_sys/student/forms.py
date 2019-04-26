from django import forms

from .models import Student
# 初步实现如下  由于大部分相等，故采用简单方法
# class StudentForm(forms.Form):
#     SEX_ITEMS = [
#         (1, '男'),
#         (2, '女'),
#         (3, '未知')
#     ]
#     STAUTS_ITEMS = [
#         (0, '申请中'),
#         (1, '已通过'),
#         (2, '已拒绝'),
#     ]
#
#     name = forms.CharField(max_length=128, verbose_name='姓名')
#     sex = forms.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
#     profession = forms.CharField(max_length=128, verbose_name='职业')
#     email = forms.EmailField(max_length=128, verbose_name='邮箱')
#     qq = forms.CharField(max_length=128, verbose_name='QQ')
#     phone = forms.CharField(max_length=128, verbose_name='手机')
#
#     status = forms.IntegerField(choices=STAUTS_ITEMS, default=0, verbose_name='审核状态')
#     created_time = forms.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')


class StudentForm(forms.ModelForm):

    # def clean_qq(self):
    #     # 把qq更改类型
    #     clean_data = self.cleaned_data['qq']
    #     if not clean_data.isdight():                        # 设置格式验证，可以使re
    #         raise forms.ValidationError('必须全部是数字！')
    #
    #     return int(clean_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status'
        )

