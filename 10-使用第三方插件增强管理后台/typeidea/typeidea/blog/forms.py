from dal import autocomplete
from django import forms
from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=autocomplete.ModelSelect2Multiple(url='caregoryautocomplete'),
                                      label='分类')
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tagautocomplete'),
        label='标签'
    )

    class Meta:
        model = Post
        fields = ('Category', 'tag', 'title', 'desc', 'conent', 'status')

