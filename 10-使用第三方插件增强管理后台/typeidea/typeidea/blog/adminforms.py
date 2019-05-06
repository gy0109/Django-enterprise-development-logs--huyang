from django import forms
from dal import autocomplete
from django import forms
from .models import Category, Tag, Post
from ckeditor.widgets import CKEditorWidget


# Form 是对用户输入以及model中要展示的数据的抽象


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, label='摘gdg要', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=autocomplete.ModelSelect2Multiple(url='caregoryautocomplete'),
                                      label='分类')
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tagautocomplete'),
        label='标签'
    )
    content = forms.CharField(widget=CKEditorWidget(), label='正文', required=True)

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'description', 'content', 'status')










