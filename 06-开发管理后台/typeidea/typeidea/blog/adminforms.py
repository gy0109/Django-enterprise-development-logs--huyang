from django import forms


# Form 是对用户输入以及model中要展示的数据的抽象


class PostAdminForm(forms.ModelForm):
    descripition = forms.CharField(widget=forms.Textarea, label='摘要', required=False)









