from django import forms
from dal import autocomplete
from django import forms
from .models import Category, Tag, Post
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Form 是对用户输入以及model中要展示的数据的抽象


class PostAdminForm(forms.ModelForm):
    descripition = forms.CharField(widget=forms.TextInput, label='摘要', required=False)  # required是否必须填
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=autocomplete.ModelSelect2(url='categoryautocomplete'),
                                      label='分类')
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tagautocomplete'),
        label='标签'
    )
    # content = forms.CharField(widget=CKEditorWidget(), label='正文', required=True)
    # 提供图片加载
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'descripition', 'content', 'status')










