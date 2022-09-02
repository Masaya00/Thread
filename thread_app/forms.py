from django import forms

class ThreadForm(forms.Form):
    thread_name = forms.CharField(label='スレッド名', widget=forms.TextInput(attrs={'placeholder': 'スレッド名を入力してください。'}))

class CommentForm(forms.Form):
    content = forms.CharField(label='コメント', widget=forms.Textarea(attrs={'placeholder': 'コメントを入力してください'}))