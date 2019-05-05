from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={
                'class': 'form-control',
                'style': 'width: 60%;'
            }
        )
    )

    email = forms.EmailField(
        label='email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width:60%;'
            }
        )
    )

    website = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'from-control',
                'style': 'width: 60%;'
            }
        )
    )

    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'from-control',
                'style': 'width: 60%;'
            }
        )
    )

    def clean_content(self):
        context = self.cleaned_data.get('content')
        if len(context) < 10:
            raise forms.ValidationError('内容长度过短')
        return context

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
