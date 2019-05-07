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
    content = forms.CharField(widget=forms.HiddenInput(), label='正文', required=True)
    content_md = forms.CharField(widget=forms.Textarea(), label='正文', required=True)
    # 提供图片加载
    content_ck = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'descripition', 'is_md', 'content', 'content_ck', 'content_md', 'status')

    def __init__(self, instance=None, initial=None, **kwargs):
        initial = initial or ()
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content
        super().__init__(instance=instance, initial=initial, **kwargs)

    def clean(self):
        is_md = self.cleaned_data.get('is_md')
        if is_md:
            content_field_name = 'contend_md'
        else:
            content_field_name = 'contend_mk'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name, '必填项')
            return

        self.cleaned_data['content'] = content
        return super().clean()

    class Media:
        js = ('js/post_editor.js')







