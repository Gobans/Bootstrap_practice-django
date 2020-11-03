from .models import Ask
from django import forms


class AskForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Ask
        fields = ('title','body','useremail','username')
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-title', }),
        'body': forms.Textarea(attrs={
            'class': 'form-body', }),
        'useremail': forms.EmailInput(attrs={
            'class': 'form-useremail',}),
        'username': forms.TextInput(attrs={
            'class': 'form-username',}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlegth'] = 100

