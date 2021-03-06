from django import forms


class TopicForm(forms.Form):
    value = forms.CharField(
        max_length=50,
        required=True,
        label='Topic',
        widget=forms.TextInput({
                'placeholder': '추가할 Topic을 입력하세요'
        })
    )
