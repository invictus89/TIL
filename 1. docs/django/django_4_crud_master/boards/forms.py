from django import forms
from .models import Board

# class BoardForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'content-type',
#                 'rows': 5,
#                 'cols': 50,
#                 'placeholder': 'Enter the content',
#             }
#         )
#     )

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(attrs={
            'placeholder': 'Enter the title',
        })
    )

    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(attrs={
            'placeholder' : 'Enter the contents',
            'rows': 5,
            'cols': 20,
        })
    )

    class Meta: # data 를 설명하기 위한 data - meta data
        model = Board
        fields = ('title', 'content') # tuple, list both OK
        #fields = '__all__'
        #exclude = ('title',)
        